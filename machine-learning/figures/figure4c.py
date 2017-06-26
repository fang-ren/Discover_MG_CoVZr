# -*- coding: utf-8 -*-
"""
Plot the formation enthalpy predicted with 
    - Trained on meltspinning and sputtering GFA, with the new CoVZr data
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
from ternary_helper import interpolation_ternary, make_cmap, interpolate_probabilities

# Important variables to change
path = os.path.join('..','3_with-CoVZr-data','plots')
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
                       sv=True, svpth=save_path, svflnm='Figure4c.png',
                       cbl='Liklihood (GFA = True)', vmin = 0.5, vmax = 1, cmap=make_cmap(), cb=True, style='h')
