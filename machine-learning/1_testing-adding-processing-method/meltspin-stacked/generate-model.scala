import magpie.attributes.generators.ModelPredictionAttributeGenerator
import magpie.data.Dataset
import magpie.data.utilities.filters.AttributeFilter
import magpie.data.utilities.splitters.FilterSplitter
import magpie.models.classification.WekaClassifier
import magpie.utility.UtilityOperations
import scala.collection.JavaConversions._
import weka.classifiers.AbstractClassifier
import weka.classifiers.meta.CVParameterSelection

// Load in dataset used to train model
val trainDataset = UtilityOperations.loadState("../all_data.obj").asInstanceOf[Dataset]

// Make a filter for keeping only entries with the sputtering condition
val filter = new AttributeFilter()
filter.train(trainDataset)
filter.setExclude(false)
filter.setOptions("processing", "=", "0")

val splitter = new FilterSplitter()
splitter.setFilter(filter)

UtilityOperations.saveState(splitter, "splitter.obj")

// Split off the melt spinning and sputtring data
val List(trainDataMS : Dataset, trainDataSp : Dataset) = splitter.split(trainDataset).toList

println(s"[Status] Generated MS-only training data. Size: ${trainDataMS.NEntries}")

// Generate a model to predict melt-spinning GFA
val treeTuner = new CVParameterSelection()
treeTuner.setClassifier(AbstractClassifier.forName("trees.RandomForest", Array[String]("-I", "200", "-num-slots", "0")))
treeTuner.addCVParameter("K 8 17 10")
treeTuner.buildClassifier(trainDataMS.clone().transferToWeka(true, true))
println(s"[Status] Tuned RF model on MS data: " + treeTuner.getBestClassifierOptions().toList)

val modelMS = new WekaClassifier("trees.RandomForest", treeTuner.getBestClassifierOptions())
modelMS.setFilter(filter)
modelMS.train(trainDataMS)
UtilityOperations.saveState(modelMS, "model-ms_only.obj")
UtilityOperations.saveState(trainDataMS.createTemplate(), "data-ms_only.obj")

// Use this to generate a model to generate attributes for sputtering models
val msOutputGenerator = new ModelPredictionAttributeGenerator()
msOutputGenerator.setModel("meltspinningGFA", modelMS, trainDataMS)

msOutputGenerator.addAttributes(trainDataSp)
treeTuner.buildClassifier(trainDataSp.clone().transferToWeka(true, true))
println(s"[Status] Tuned RF model on Sp data: " + treeTuner.getBestClassifierOptions().toList)

val modelSp = new WekaClassifier("trees.RandomForest", treeTuner.getBestClassifierOptions())
modelSp.train(trainDataSp)
UtilityOperations.saveState(msOutputGenerator, "atgen-ms.obj")
UtilityOperations.saveState(modelSp, "model-sp_only.obj")
UtilityOperations.saveState(trainDataSp.createTemplate(), "data-sp_only.obj")
