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
import scipy
from scipy import interpolate


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\Theory\\'
save_path = path

filename = path + 'All_Data_low.csv'

data = np.genfromtxt(filename, delimiter=',', skip_header = 1)


Co = data[:,0]
V = data[:,1]
Zr = data[:,2]

## theory
# structural_high = data[:,3]
# structural_low = data[:,4]
# thermodynamic = data[:,5]
#
# ternary_data = np.concatenate(([Co],[V],[Zr],[structural_high]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('Co', 'V', 'Zr'), scale=100,
#                              sv=True, svpth=save_path, svflnm='quasicrystals_high',
#                              cbl='Scale', vmax=1.8, vmin=-1.2, cmap='jet_r', cb=True, style='h')
#
# ternary_data = np.concatenate(([Co],[V],[Zr],[structural_low]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('Co', 'V', 'Zr'), scale=100,
#                              sv=True, svpth=save_path, svflnm='quasicrystals_low',
#                              cbl='Scale', vmax=1.8, vmin=-1.2, cmap='jet_r', cb=True, style='h')
#
# ternary_data = np.concatenate(([Co],[V],[Zr],[thermodynamic]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('Co', 'V', 'Zr'), scale=100,
#                              sv=True, svpth=save_path, svflnm='thermodynamic',
#                              cbl='Scale', vmax=1.8, vmin=-1.2, cmap='jet_r', cb=True, style='h')

## data
FWHM = data[:, 3]
labels = data[:, 4]

ternary_data = np.concatenate(([Co],[V],[Zr],[FWHM]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='peak_width_low',
                       cbl='Scale', vmin = 0.12, vmax = 0.79, cmap='jet_r', cb=True, style='h')


ternary_data = np.concatenate(([Co],[V],[Zr],[labels]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='glass_or_crystal_low',
                       cbl='Scale', vmax = 1.4, vmin = -0.1, cmap='jet_r', cb=True, style='h')
