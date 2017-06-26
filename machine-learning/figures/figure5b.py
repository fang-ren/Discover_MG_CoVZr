# -*- coding: utf-8 -*-
"""
Plot the formation enthalpy predicted with 
    - Trained on meltspinning and sputtering GFA
    - Accounts for processing with "stacked" approach
    - Uses Yang and Laws theories
    
@author: fangren
"""

# Load in libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy import interpolate
import imp
import os
import pandas as pd
from ternary_helper import interpolation_ternary, make_cmap

# Important variables to change
path = os.path.join('..','3_with-CoVZr-data','plots')
save_path = os.path.join('..','..','figures')

# Load in the ML results
filename_new = os.path.join(path, 'FeNbTi.csv')
data = pd.read_csv(filename_new)

Fe = data['X_Fe']*100
Nb = data['X_Nb']*100
Ti = data['X_Ti']*100
probability = data['probability']


# Interpolate probabilities
probability_func = interpolate.Rbf(Fe, Nb, Ti, probability, function='multiquadric',
                                       smooth=0.3)

metal1_range = np.arange(0, 100, 1.25)
metal2_range = np.arange(0, 100, 1.25)

metal1 = []
metal2 = []
metal3 = []

probability_interpolate = []

for i in metal1_range:
    for j in metal2_range:
        if i + j <= 100 and i+j >= 0:
            try:
                metal1.append(i)
                metal2.append(j)
                metal3.append(100-i-j)
                probability_interpolate.append(float(probability_func(i, j, (100-i-j))))
            except(NbalueError):
                continue


# Make a new colormap that has alpha of 0.5 below 0.95%
                
ternary_data = np.concatenate(([metal1],[metal2],[metal3],[probability_interpolate]), axis = 0)
ternary_data = np.transpose(ternary_data)

interpolation_ternary(ternary_data, tertitle='',  labelNames=('Fe', 'Nb', 'Ti'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure5b.png',
                       cbl='Liklihood (GFA = True)', vmin = 0.5, vmax = 1, cmap=make_cmap(), cb=True, style='h')
