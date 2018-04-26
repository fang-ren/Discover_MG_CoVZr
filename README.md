# Discovering Metallic Glasses with HiTp Experiment and Machine Learning
This repository contains scripts necessary to recreate the results from ["Accelerated Discovery of Metallic Glasses through Iteration of Machine Learning and High-Throughput Experiments,"](http://advances.sciencemag.org/content/4/4/eaaq1566) a paper authored by Fang Ren, Logan Ward, Travis Williams, Kevin Laws, Chris Wolverton, Jason Hattrick-Simpers, and Apurva Mehta. 

The exact version of the code and results used in our paper are available on the [Materials Data Facility](http://dx.doi.org/doi:10.18126/M2B06M).

## Running the Scripts

There are a few options for running the software in this repository.

*Option 1*: Install the software on your own machine. See directions in the [`machine-learning/README.txt`](machine-learning) for the required sofware.

*Option 2*: Use Docker. Build the container described in [`Dockerfile`](./Dockerfile)

*Option 3*: Use [WholeTale](https://dashboard.wholetale.org/tale/view/5ad4eb52f4b80b00018d92e1). The data and software for this study are published on [WholeTale](http://wholetale.org/), which will let you run them without installing any software.

Regardless of the method you use to run the software, you can recreate the entire study by calling `./run-all.bs` in the `machine-learning` directory.
