# -*- coding: utf-8 -*-
"""
Plot the formation enthalpy predicted by our original model:
    - Trained on meltspinning GFA
    - Uses Yang and Laws theories

@author: fangren
"""

# Load in libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import imp
import os
import pandas as pd
from ternary_helper import interpolation_ternary, make_cmap

# Important variables to change
path = os.path.join('..','0_original-model','plots')
save_path = os.path.join('..','..','figures')

# Load in the ML results
filename_new = os.path.join(path, 'CoVZr.csv')
data = pd.read_csv(filename_new)

Co = data['X_Co']*100
V = data['X_V']*100
Zr = data['X_Zr']*100
probability = data['probability']


# Interpolate probabilities
probability_func = interpolate.Rbf(Co, V, Zr, probability, function='multiquadric',
                                       smooth=0.3)

metal1_range = np.linspace(0, 100, 63)
metal2_range = np.linspace(0, 100, 63)

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
            except(ValueError):
                continue


# Make a new colormap that lightens colors color
new_cmap = make_cmap()
                    
ternary_data = np.concatenate(([metal1],[metal2],[metal3],[probability_interpolate]), axis = 0)
ternary_data = np.transpose(ternary_data)

interpolation_ternary(ternary_data, tertitle='',  labelNames=('Co', 'V', 'Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure2c1.png',
                       cbl='Liklihood (GFA = True)', vmin = 0.5, vmax = 1, cmap=new_cmap, cb=True, style='h')
