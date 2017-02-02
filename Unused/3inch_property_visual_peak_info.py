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


#path = 'C:\Research_FangRen\Data\July2016\CoVZr_ternary\masterfiles\high\plotting\\'

path = 'C:\Research_FangRen\Data\July2016\CoVZr_ternary\masterfiles\high\plotting\\'

def twoD_visualize(path):
    """
    create three lists for plotting: plate_x, plate_y, ROI1, ROI2, ROI3...
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
        if basename(filename)[0] == '8':
            print basename(filename)
            data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            metal1 = data[:,69]
            metal2 = data[:,70]
            metal3 = data[:,71]
            peak_position = data[:,60]
            peak_width = data[:,61] 
            peak_intensity = data[:,62]
    return metal1, metal2, metal3, peak_position, peak_width, peak_intensity

                 
metal1, metal2, metal3, peak_position, peak_width, peak_intensity = twoD_visualize(path)


ternary_data = np.concatenate(([metal1],[metal2],[metal3],[peak_width]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='peak_width_ternary',
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
                       sv=True, svpth=path, svflnm='glass_or_crystal',
                       cbl='Scale', vmin = 0.2, vmax = 3.2, cmap='jet', cb=True, style='h')



ternary_data = np.concatenate(([metal1],[metal2],[metal3],[peak_intensity]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='peak_intensity_ternary',
                       cbl='Scale', vmin=137, vmax=1420, cmap='jet', cb=True, style='h')
                       

ternary_data = np.concatenate(([metal1],[metal2],[metal3],[peak_position]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='peak_position_ternary',
                       cbl='Scale', vmin=2.51, vmax=3.14, cmap='jet', cb=True, style='h')

plt.close("all")

