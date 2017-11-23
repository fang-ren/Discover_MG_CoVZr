This directory contains a repeat of the earlier test used to determine the best 
method for accounting for processing method in our ML models. This time, we 
are including our new HiTp data to study whether the best method changes.

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
23 November 2017
