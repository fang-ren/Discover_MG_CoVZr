# -*- coding: utf-8 -*-
"""
Created on Wed July 13 2016

@author: fangren
"""


import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from os.path import basename
import imp

plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")

path = ''

metal1 = [np.nan]
metal2 = [np.nan]
metal3 = [np.nan]
peak_width = [np.nan]

ternary_data = np.concatenate(([metal1],[metal2],[metal3],[peak_width]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=False, svpth=path, svflnm='peak_width_ternary',
                       cbl='Scale', vmin = 0.13, vmax = 0.406, cmap='jet_r', cb=False, style='h')

