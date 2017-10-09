import magpie.attributes.selectors.UserSpecifiedExcludingAttributeSelector
import magpie.data.Dataset
import magpie.models.classification.WekaClassifier
import magpie.utility.UtilityOperations
import scala.collection.JavaConversions._
import weka.classifiers.AbstractClassifier
import weka.classifiers.meta.CVParameterSelection

// Load in dataset used to train model
val trainDataset = UtilityOperations.loadState("../all_data.obj").asInstanceOf[Dataset]

// Make selector for removing the "processing" variable
val selector = new UserSpecifiedExcludingAttributeSelector()
selector.selectAttributes(List[String]("processing"))

println(s"[Status] Training attribute selector")
selector.train(trainDataset)
selector.run(trainDataset)

// Tune a random forest model
val treeTuner = new CVParameterSelection()
treeTuner.setClassifier(AbstractClassifier.forName("trees.RandomForest", Array[String]("-I", "200", "-num-slots", "0")))
treeTuner.setDebug(true)
treeTuner.addCVParameter("K 8 17 10")

selector.run(trainDataset)

println(s"[Status] Tuning random forest model")
treeTuner.buildClassifier(trainDataset.transferToWeka(true, true))

// Make the final model and save it to disk
val model = new WekaClassifier("trees.RandomForest", treeTuner.getBestClassifierOptions())
model.setAttributeSelector(selector)
UtilityOperations.saveState(model, "model.obj")
