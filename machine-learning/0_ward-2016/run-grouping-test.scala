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

// Load in the LB set
val data = UtilityOperations.loadState("gfa-training-data.obj").asInstanceOf[Dataset];

// Get list of all phase diagrams
var phaseDiagrams = Set[Seq[Int]]();
for (entry <- data.getEntries()) {
    val elems = entry.asInstanceOf[CompositionEntry].getElements().toSeq;
    if (elems.length == 3) {
        phaseDiagrams += elems
    }
}
println(s"Number of phase diagrams: ${phaseDiagrams.size()}");

// Load in the model
val model = UtilityOperations.loadState("gfa-model.obj").asInstanceOf[BaseModel]
    
// Run a large CV test
val cvData = data.emptyClone()
for (diagram <- phaseDiagrams) {
    // Separate training and test set
    val testFilter = new PhaseDiagramExclusionFilter();
    testFilter.setElementListByIndex(diagram.toArray);
    
    val testSplitter = new FilterSplitter();
    testSplitter.setFilter(testFilter);
    
    // Get the training and test data
    val List(testData : Dataset, trainData : Dataset) = testSplitter.split(data, true).toList;
    println(s"${diagram.map(x => LookupData.ElementNames(x)).mkString("-")}. Training size: ${trainData.NEntries} Test size: ${testData.NEntries()}");
    
    // Retrain and test model
    model.train(trainData);
    model.run(testData);
    cvData.addEntries(testData, true);
    
    // Make sure cvData does not contain any attributes
    cvData.clearAttributes();
}

cvData.saveCommand("cv-data-grouping", "json");
