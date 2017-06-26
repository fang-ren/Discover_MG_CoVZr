import magpie.attributes.selectors.UserSpecifiedExcludingAttributeSelector
import magpie.data.Dataset
import magpie.data.utilities.splitters.AttributeIntervalSplitter
import magpie.models.classification.SplitClassifier
import magpie.models.classification.WekaClassifier
import magpie.utility.UtilityOperations
import scala.collection.JavaConversions._
import weka.classifiers.AbstractClassifier
import weka.classifiers.meta.CVParameterSelection

// Load in dataset used to train model
val trainDataset = UtilityOperations.loadState("../all_data.obj").asInstanceOf[Dataset]

// Split data into each processing condition
val splitter = new AttributeIntervalSplitter()
splitter.setAttributeName("processing")
splitter.setBinEdges(Array[Double]{0.5})
splitter.train(trainDataset)
val List(sputteringData : Dataset, meltspinData : Dataset) = splitter.split(trainDataset, true).toList

// Tune a random forest model on each processing condition
val treeTuner = new CVParameterSelection()
treeTuner.setClassifier(AbstractClassifier.forName("trees.RandomForest", Array[String]("-I", "200", "-num-slots", "0")))
treeTuner.setDebug(true)
treeTuner.addCVParameter("K 8 17 10")

//    Sputtering 
println(s"[Status] Tuning random forest model on sputteringData")
treeTuner.buildClassifier(sputteringData.transferToWeka(true, true))
val sputteringModel = new WekaClassifier("trees.RandomForest", treeTuner.getBestClassifierOptions())

//    Meltspin
println(s"[Status] Tuning random forest model on sputteringData")
treeTuner.buildClassifier(meltspinData.transferToWeka(true, true))
val meltspinModel = new WekaClassifier("trees.RandomForest", treeTuner.getBestClassifierOptions())

// Make the final model and save it to disk
val model = new SplitClassifier()
model.setPartitioner(splitter)
model.setModel(0, sputteringModel)
model.setModel(1, meltspinModel)
UtilityOperations.saveState(model, "model.obj")
