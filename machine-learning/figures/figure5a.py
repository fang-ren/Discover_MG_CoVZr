# -*- coding: utf-8 -*-
"""
Plot the formation enthalpy predicted with 
    - Trained on meltspinning and sputtering GFA
    - Accounts for processing with "stacked" approach
    - Uses Yang and Laws theories
    
@author: fangren, Logan Ward
"""

# Load in libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy import interpolate
import imp
import os
import pandas as pd
import sys
from ternary_helper import make_cmap, interpolate_probabilities

sys.path.append(os.path.join('..','..'))
from scripts.figure_plotters.plotTernary import plt_ternary_save as interpolation_ternary


# Important variables to change
path = os.path.join('..','4_with-CoVZr-data','plots')
save_path = os.path.join('..','..','figures')

# Load in the ML results
filename_new = os.path.join(path, 'FeNbTi.csv')
data = pd.read_csv(filename_new)

Fe = data['X_Fe']*100
Nb = data['X_Nb']*100
Ti = data['X_Ti']*100
probability = data['probability']

# Load in the log loss
with open(os.path.join('..','4_with-CoVZr-data','run-HiTp-data.out')) as fp:
    # Get the lines with "log-loss" data
    data_lines = [ x for x in fp if 'Log-loss' in x ]

    # The first is CoVZr, second is FeNbTi
    log_loss = float(data_lines[1].split()[-1])

# Interpolate probabilities
ternary_data = interpolate_probabilities(Fe, Ti, Nb, probability)
interpolation_ternary(ternary_data, tertitle='',  labelNames=('Fe', 'Ti', 'Nb'), scale=100,
                       sv=True, svpth=save_path, svflnm='/Figure5_CoVZr-gen2.png',
                       cbl='Likelihood (GFA = True)', vmin = 0.5, vmax = 1, cmap=make_cmap(), cb=True, style='h',
                       other_labels=[(50, -17.5, 'Log-loss: %.3f'%log_loss)])
