## -*- coding: utf-8 -*-
#"""
#Created on Wed July 13 2016
#
#@author: fangren
#"""


import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from os.path import basename
import imp
from scipy import polyfit


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\masterfiles\\low\\plotting\\'

def twoD_visualize(path):
    """
    create three lists for plotting: plate_x, plate_y, ROI1, ROI2, ROI3...
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
        if basename(filename)[0] == 'P':
            print basename(filename)
            data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            ROI1 = data[:,15]
            ROI2 = data[:,16]
            ROI3 = data[:,17]
            ROI4 = data[:,18]
            ROI5 = data[:,19]
            ROI6 = data[:,20]
            metal1 = data[:,57]*100
            metal2 = data[:,58]*100
            metal3 = data[:,59]*100
    return ROI1, ROI2, ROI3, ROI4, ROI5, ROI6, metal1, metal2, metal3

                 
ROI1, ROI2, ROI3, ROI4, ROI5, ROI6, metal1, metal2, metal3 = twoD_visualize(path)


#ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI1]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='ROI1',
#                       cbl='Scale', vmin = 772, vmax = 1211222.0, cmap='jet', cb=True, style='h')
#
#
ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI2]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='ROI2_ternary',
                       cbl='Scale', vmin = 772, vmax = 1051932.0, cmap='jet', cb=True, style='h')
                       
ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI3]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='ROI3_ternary',
                       cbl='Scale', vmin = 772, vmax = 150579.0, cmap='jet', cb=True, style='h')
                       
ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI4]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='ROI4_ternary',
                       cbl='Scale', vmin = 772, vmax = 11192.0, cmap='jet', cb=True, style='h')
                       
#

plt.close("all")

