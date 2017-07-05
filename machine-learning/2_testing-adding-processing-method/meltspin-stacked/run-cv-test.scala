import magpie.attributes.generators.ModelPredictionAttributeGenerator
import magpie.data.Dataset
import magpie.data.utilities.splitters.BaseDatasetSplitter
import magpie.data.utilities.generators.PhaseDiagramCompositionEntryGenerator
import magpie.models.BaseModel
import magpie.utility.UtilityOperations
import scala.collection.JavaConversions._

// Load in the test set
val data = UtilityOperations.loadState("../all_data.obj").asInstanceOf[Dataset]

// Split data and test data into sputtering and meltspinng
val splitter = UtilityOperations.loadState("splitter.obj").asInstanceOf[BaseDatasetSplitter]

// Load in the models and attribute generator
val modelMs = UtilityOperations.loadState("model-ms_only.obj").asInstanceOf[BaseModel]
val msModelOutput = UtilityOperations.loadState("atgen-ms.obj").asInstanceOf[ModelPredictionAttributeGenerator]
val modelSp = UtilityOperations.loadState("model-sp_only.obj").asInstanceOf[BaseModel]

// Run a large CV test
val cvData = data.emptyClone()

for (seed <- 1 to 250) {
	// Get a random subset
	val trainDataset = data.clone()
	val testDataset = trainDataset.getRandomSplit(0.2, seed, true);
	
	// Split train and test dataset into melt spinning and sputtering
	val List(testMs : Dataset, testSp : Dataset) = splitter.split(testDataset).toList
	val List(trainMs: Dataset, trainSp : Dataset) = splitter.split(trainDataset).toList
	
	// Train the melt spin model, and run on the melt spin data
	modelMs.train(trainMs)
	modelMs.run(testMs)
	cvData.addEntries(testMs, true)
	
	// Use this model to generate new attributes for the sputtering
	msModelOutput.setModel("meltspinningGFA", modelMs, trainMs)
	msModelOutput.addAttributes(trainSp)
	msModelOutput.addAttributes(testSp)
	
	// Train and run the sputtering model
	modelSp.train(trainSp)
	modelSp.run(testSp)
	cvData.addEntries(testSp, true)
	
	// Make sure cvData does not contain any attributes
	cvData.clearAttributes()
}

cvData.saveCommand("cv_test_data", "json")
