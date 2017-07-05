This directory holds files used to explore how best to train a model that takes the
processing method used to create a metallic glass in to account by performing 
80/20%x250 train/test crossvalidation.

We test several different strategies

	1) [no-processing] - Don't distinguish by processing condition
		This is a strawman / baseline
	2) [process-variable] - Include a binary variable that defines the casting method: melt-spin or sputtering
	3) [split-model] - Train a separate model on meltspin and sputting data
	4) [meltspin-stacked] - Train a model on only melt spin data, use as input into sputtering

To run all of the tests, call "./run-all.bs"

Run the following Jupyter notebooks to analyze results
	analyze-cv-results.ipynb - Analyze the results from the hold-out test

Logan Ward
7 March 2017
