# -*- coding: utf-8 -*-
"""
Plot the formation enthalpy predicted by our original model:
    - Trained on meltspinning GFA
    - Uses Yang and Laws theories

@author: fangren, Logan Ward
"""

# Load in libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import imp
import os
import pandas as pd
import sys
from ternary_helper import make_cmap, interpolate_probabilities

sys.path.append(os.path.join('..','..'))
from scripts.figure_plotters.plotTernary import plt_ternary_save as interpolation_ternary

# Important variables to change
path = os.path.join('..','0_ward-2016','plots')
save_path = os.path.join('..','..','figures')

# Load in the ML results
filename_new = os.path.join(path, 'CoVZr.csv')
data = pd.read_csv(filename_new)

Co = data['X_Co']*100
V = data['X_V']*100
Zr = data['X_Zr']*100
probability = data['probability']


# Interpolate probabilities
ternary_data = interpolate_probabilities(Co, V, Zr, probability)
interpolation_ternary(ternary_data, tertitle='',  labelNames=('Co', 'V', 'Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='\Figure2a.png',
                       cbl='Likelihood (GFA = True)', vmin = 0.5, vmax = 1, cmap=make_cmap(), cb=True, style='h')
