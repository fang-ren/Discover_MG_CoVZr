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



plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\masterfiles\\low\\'
save_path = path + 'plots\\'

basename1 = 'CLEANED_Sample9_master_metadata.csv'
basename2 = 'CLEANED_Sample10_master_metadata.csv'
basename3 = 'CLEANED_Sample18_master_metadata.csv'

filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)
data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)
data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)

data = np.concatenate((data1, data2, data3))

metal1 = data[:,57]*100
metal2 = data[:,58]*100
metal3 = data[:,59]*100
peak_position = data[:,60]
peak_width = data[:,61]
peak_intensity = data[:,62]



ternary_data = np.concatenate(([metal1],[metal2],[metal3],[peak_width]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='peak_width_ternary_all',
                       cbl='Scale', vmin = 0.34, vmax = 0.8, cmap='jet_r', cb=True, style='h')

labels = []
for pw in peak_width:
    if pw < 0.23:
        label = 3
    elif pw > 0.56:
        label = 1
    else:
        label = 2
    labels.append(label)

ternary_data = np.concatenate(([metal1],[metal2],[metal3],[labels]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='glass_or_crystal_all',
                       cbl='Scale', vmin = 0.2, vmax = 3.2, cmap='jet', cb=True, style='h')



ternary_data = np.concatenate(([metal1],[metal2],[metal3],[peak_intensity]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='peak_intensity_ternary_all',
                       cbl='Scale', vmin=137, vmax=1420, cmap='jet', cb=True, style='h')
                       

ternary_data = np.concatenate(([metal1],[metal2],[metal3],[peak_position]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='peak_position_ternary_all',
                       cbl='Scale', vmin=2.51, vmax=3.14, cmap='jet', cb=True, style='h')

plt.close("all")


