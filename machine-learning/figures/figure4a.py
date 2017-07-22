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
import os
import pandas as pd
import sys
from ternary_helper import make_cmap, interpolate_probabilities

sys.path.append(os.path.join('..','..'))
from scripts.figure_plotters.plotTernary import plt_ternary_save as interpolation_ternary


# Important variables to change
path = os.path.join('..','3_with-processing-method','plots')
save_path = os.path.join('..','..','figures')

# Load in the ML results
filename_new = os.path.join(path, 'CoVZr.csv')
data = pd.read_csv(filename_new)

Co = data['X_Co']*100
V = data['X_V']*100
Zr = data['X_Zr']*100
probability = data['probability']

# Load in the log loss
with open(os.path.join('..','3_with-processing-method','run-HiTp-data.out')) as fp:
    # Get the lines with "log-loss" data
    data_lines = [ x for x in fp if 'Log-loss' in x ]

    # The first is CoVZr, second is FeNbTi
    log_loss = float(data_lines[0].split()[-1])

# Interpolate probabilities
ternary_data = interpolate_probabilities(Co, V, Zr, probability)
interpolation_ternary(ternary_data, tertitle='',  labelNames=('Co', 'V', 'Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='/Figure4a.png',
                       cbl='Likelihood (GFA = True)', vmin = 0.5, vmax = 1, cmap=make_cmap(), cb=True, style='h',
                       other_labels=[(50, -17.5, 'Log-loss: %.3f'%log_loss)])
