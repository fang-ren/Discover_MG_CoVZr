__author__ = "Travis Williams. Logan Ward"
# University of South Carolina
# Jason Hattrick-Simpers group
# Starting Date: June, 2016

from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
from scipy import interpolate
import numpy as np
import os

import ternary

def interpolate_probabilities(a,b,c,p):
    """Prepare probabilities for plotting with ternary's heatmap
    
    Inputs:
        a,b,c - Fractions of metal A,B,C
        p - Probability function to be interpolated
    Output:
        Probabilities at a finer spacing all over the ternary, in a form that 
    """
        
    probability_func = interpolate.Rbf(a,b,c,p, function='multiquadric',
                                           smooth=0.3)

    metal1_range = np.linspace(0, 100, 63, endpoint=False) # Makes the nicest plots
    metal2_range = metal1_range[:] # Copy

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

    ternary_data = np.concatenate(([metal1],[metal2],[metal3],[probability_interpolate]), axis = 0)
    return np.transpose(ternary_data)

def make_cmap(base='viridis_r', scale_factor=1.5, cutoff=0.9, adjust_factor=0.1):
    """Make a colormap that this scaled to emphasize the top of the range.
    
    Two kinds of emphasis:
        1) Scaling the colormap to have a stronger gradient at the top
        2) Making the colors below a treshold lighter
        
    Inputs:
        base - str, base color map name
        scale_factor - float, how much to exaggerate the range at the top (larger value -> larger scaling)
        cutoff - float, treshold below which to lighten colors (0-1)
        adjust_factor - float, how much to dampen colors (0-1)
    Returns:
        Colormap
    """
    
    # Get the base colormap
    v = cm.get_cmap('viridis_r')
    
    # Scale it
    new_list = v(np.linspace(0,1,300) ** scale_factor)

    # Apply cutoff
    new_list[:int(len(new_list)*cutoff),:3] += (1 - new_list[:int(len(new_list)*cutoff),:3]) * adjust_factor
    return ListedColormap(new_list, name='%s_scaled'%base)
