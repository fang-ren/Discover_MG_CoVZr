These directories contain the code necessary to replicate the machine learning work in this study.

Running all scripts with require:

	Java Development Kit >= 1.7
	Scala >= 2.11.8
	Python >= 2.7, with the packages listed in "requirements.txt"

There should be several subdirectories:

	datasets - Datasets needed to train the model [Note: Some of these are duplicated in other parts of this SI]
	magpie - Version of Magpie (https://bitbucket.org/wolverton/magpie) used with this study
	0_original-model - ML model trained to predict melt-spinning GFA of metallic alloys
	1_testing-adding-processing-method - Test of several strategies to include processing method into ML model
	2_with-processing-method - ML model trained to predict sputtering GFA
	3_with-CoVZr-data - ML model from "2" trained with newly-collected data of the Co-V-Zr system

If you are running a version of Linux with the bash shell, you can use two scripts to run all of the tests in this paper:

./install.bs - Compiles Magpie, installs Python packages
./run-all.bs - Runs all tests
