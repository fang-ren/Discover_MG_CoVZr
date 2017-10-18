# -*- coding: utf-8 -*-
"""
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
old_path = os.path.join('..','3_with-theories','plots')
new_path = os.path.join('..','4_with-CoVZr-data','plots')
save_path = os.path.join('..','..','figures','figure6')

for gen,path in enumerate([old_path, new_path]):
    for order,tern in enumerate([['Co', 'V', 'Zr'], ['Fe','Ti','Nb'],['Co','Fe','Zr'],['Co','Ti','Zr']]):
        name = ''.join(tern)
        # Load in the ML results
        filename_new = os.path.join(path, '%s.csv'%name)
        data = pd.read_csv(filename_new)

        A = data['X_%s'%tern[0]]*100
        B = data['X_%s'%tern[1]]*100
        C = data['X_%s'%tern[2]]*100
        probability = data['probability']

        # Load in the log loss
        with open(os.path.join(path, '..', 'run-HiTp-data.out')) as fp:
            # Get the lines with "log-loss" data
            data_lines = [ x for x in fp if 'Log-loss' in x ]

            # See run-HiTp-data.in for order
            log_loss = float(data_lines[order].split()[-1])

        # Interpolate probabilities
        ternary_data = interpolate_probabilities(A, B, C, probability)
        interpolation_ternary(ternary_data, tertitle='',  labelNames=tern, scale=100,
                               sv=True, svpth=save_path, svflnm='/Figure6_%s-gen%d.png'%(name, gen+1),
                               cbl='Likelihood (GFA = True)', vmin = 0.5, vmax = 1, cmap=make_cmap(), cb=True, style='h',
                               other_labels=[(50, -17.5, 'Log-loss: %.3f'%log_loss)])
