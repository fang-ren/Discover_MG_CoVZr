import magpie.attributes.generators.ModelPredictionAttributeGenerator;
import magpie.data.Dataset;
import magpie.data.materials.CompositionEntry;
import magpie.data.materials.util.LookupData;
import magpie.data.utilities.filters.{PropertyFilter, PhaseDiagramExclusionFilter};
import magpie.data.utilities.splitters.FilterSplitter;
import magpie.data.utilities.generators.PhaseDiagramCompositionEntryGenerator;
import magpie.models.BaseModel;
import magpie.utility.UtilityOperations;
import scala.collection.JavaConversions._;

// Variables to change
val templatePath = "2_with-processing-method";
val newSystems = Seq[Seq[String]](Seq("Co","V","Zr"), Seq("Fe","Ti","Nb"), Seq("Co","Fe","Zr"), Seq("Co","Ti","Zr"))

// Load in the LB set
val data = UtilityOperations.loadState(s"../${templatePath}/gfa-sputtering_training-data.obj").asInstanceOf[Dataset];

// Add in the other data
for (sys <- newSystems) {
    var temp = data.emptyClone();
    temp.importText(s"../datasets/new-data/sputtering_${sys.mkString("")}.data", null);
    temp = temp.getRandomSubset(100);
    data.combine(temp);
}
data.generateAttributes();

// Split data and test data into sputtering and meltspinng
val filter = new PropertyFilter()
filter.train(data)
filter.setExclude(false)
filter.setOptions("processing", "=", "0")

val splitter = new FilterSplitter()
splitter.setFilter(filter)
    
val List(meltSpinData : Dataset, sputterData : Dataset) = splitter.split(data).toList;
println(s"Loaded data. Sputtering size: ${sputterData.NEntries} Meltspin size: ${meltSpinData.NEntries()}");

// Get list of all phase diagrams
var phaseDiagrams = Set[Seq[Int]]();
for (entry <- sputterData.getEntries()) {
    val elems = entry.asInstanceOf[CompositionEntry].getElements().toSeq;
    if (elems.length == 3) {
        phaseDiagrams += elems
    }
}
println(s"Number of phase diagrams: ${phaseDiagrams.size()}");

// Load in the model
val model = UtilityOperations.loadState(s"../${templatePath}/gfa-model.obj").asInstanceOf[BaseModel]
model.setFilter(null);
    
// Train a model on all of the meltspin data
val modelMs = model.clone();
modelMs.train(meltSpinData);

// Run a large CV test
val cvDataNoSp = data.emptyClone()
var cvData = Seq[Dataset](data.emptyClone()); // CV data for the sputtering models
// [0] is the model with only LB, [1] is with LB+CoVZr, [2] is with LB+CoVZr+NbFeTi, etc.
for (system <- newSystems) {
    cvData = data.emptyClone() +: cvData;
}

for (diagram <- phaseDiagrams) {
    // Separate training and test set
    val testFilter = new PhaseDiagramExclusionFilter();
    testFilter.setElementListByIndex(diagram.toArray);
    
    val testSplitter = new FilterSplitter();
    testSplitter.setFilter(testFilter);
    
    // Get the training and test data
    val List(testData : Dataset, trainData : Dataset) = testSplitter.split(sputterData, true).toList;
    println(s"${diagram.map(x => LookupData.ElementNames(x)).mkString("-")}. Training size: ${trainData.NEntries} Test size: ${testData.NEntries()}");
    
    // Run the melt-spinning model 
    modelMs.run(testData)
    cvDataNoSp.addEntries(testData, true);
    
    // Run the models with all of the data
    model.train(trainData);
    model.run(testData);
    cvData.last.addEntries(testData, true);
    
    // Run the model while gradually removing data
    for ((system,i) <- newSystems.reverse.zipWithIndex) {
        // Remove that new system from the dataset
        val tempFilter = new PhaseDiagramExclusionFilter();
        tempFilter.setElementList(system.toArray);
        tempFilter.setExclude(true);
        tempFilter.filter(trainData);
        
        // Train and test the model
        model.train(trainData);
        model.run(testData);
        
        // Add to the cvData array, starting from the second to last
        cvData(cvData.length - (2 + i)).addEntries(testData, true);
    }
    
    // Make sure cvData does not contain any attributes
    cvData.foreach(_.clearAttributes());
    cvDataNoSp.clearAttributes();
}

cvDataNoSp.saveCommand("results/cv_Only_Meltspin", "json");
cvData(0).saveCommand("results/cv_LB", "json");
for (i <- 1 to newSystems.length) {
    val name = newSystems.take(i).map(_.mkString("")).mkString("+");
    cvData(i).saveCommand(s"results/cv_LB+${name}", "json");
}
