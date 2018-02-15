These directories contain the code necessary to replicate the machine learning work in this study.

Running all scripts with require:

	Java Development Kit >= 1.7
	Scala >= 2.11.8
	Python >= 3.5, with the packages listed in "requirements.txt" of the top-level directory

There should be several subdirectories:

	datasets - Datasets used to train the model
	magpie - Version of Magpie (https://bitbucket.org/wolverton/magpie) used with this study
	0_ward-2016 - ML model trained to predict melt-spinning GFA of metallic alloys
	1_testing-adding-processing-method - Test of several strategies to include processing method into ML model
	2_with-processing-method - ML model trained to predict sputtering GFA
    3_with-theories - Exploring integrating physiochemical theories into the ML model
	4_with-CoVZr-data - ML model from "3" trained with newly-collected data of the Co-V-Zr system
    5_adding-more-HiTp-data - The result of adding even more HiTp data into the training set
    6_retesting-processing-method - Testing whether the new HiTp data changes how we should incorporate processing method

If you are running a version of Linux with the bash shell, you can use two scripts to run all of the tests in this paper:

./install.bs - Compiles Magpie, installs Python packages
./run-all.bs - Runs all tests
