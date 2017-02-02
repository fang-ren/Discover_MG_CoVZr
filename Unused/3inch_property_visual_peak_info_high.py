# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 09:18:54 2016

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
import pylab
from pylab import * 


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = 'C:\Research_FangRen\Data\July2016\CoVZr_ternary\masterfiles\high\plotting\\'

def twoD_visualize(path):
    """
    create three lists for plotting: plate_x, plate_y, ROI1, ROI2, ROI3...
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
#        if basename(filename)[0] == '1':
            print basename(filename)
            data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
## top and right
#            ROI1 = np.concatenate((data[:,15][882:],data[:,15][:441]))            
#            ROI2 = np.concatenate((data[:,16][882:],data[:,16][:441]))
#            ROI3 = np.concatenate((data[:,17][882:],data[:,17][:441]))
#            ROI4 = np.concatenate((data[:,18][882:],data[:,18][:441]))
#            ROI5 = np.concatenate((data[:,19][882:],data[:,19][:441]))
#            metal1 = np.concatenate((data[:,57][882:],data[:,57][:441]))
#            metal2 = np.concatenate((data[:,58][882:],data[:,58][:441]))
#            metal3 = np.concatenate((data[:,59][882:],data[:,59][:441]))
#            peak_position = np.concatenate((data[:,60][882:],data[:,60][:441]))
#            peak_width = np.concatenate((data[:,61][882:],data[:,61][:441]))    
#            peak_intensity = np.concatenate((data[:,62][882:],data[:,62][:441]))
## top and left
#            ROI1 = np.concatenate((data[:,15][441:882],data[:,15][:441]))
#            ROI2 = np.concatenate((data[:,16][441:882],data[:,16][:441]))
#            ROI3 = np.concatenate((data[:,17][441:882],data[:,17][:441]))
#            ROI4 = np.concatenate((data[:,18][441:882],data[:,18][:441]))
#            ROI5 = np.concatenate((data[:,19][441:882],data[:,19][:441]))
#            metal1 = np.concatenate((data[:,57][441:882],data[:,57][:441]))
#            metal2 = np.concatenate((data[:,58][441:882],data[:,58][:441]))
#            metal3 = np.concatenate((data[:,59][441:882],data[:,59][:441]))
#            peak_position = np.concatenate((data[:,60][441:882],data[:,60][:441]))
#            peak_width = np.concatenate((data[:,61][441:882],data[:,61][:441]))    
#            peak_intensity = np.concatenate((data[:,62][441:882],data[:,62][:441]))
### left and right
#            ROI2 = np.concatenate((data[:,16][882:],data[:,16][441:882]))
#            ROI1 = np.concatenate((data[:,15][882:],data[:,15][441:882]))
#            ROI3 = np.concatenate((data[:,17][882:],data[:,17][441:882]))
#            ROI4 = np.concatenate((data[:,18][882:],data[:,18][441:882]))
#            ROI5 = np.concatenate((data[:,19][882:],data[:,19][441:882]))
#            metal1 = np.concatenate((data[:,57][882:],data[:,57][441:882]))
#            metal2 = np.concatenate((data[:,58][882:],data[:,58][441:882]))
#            metal3 = np.concatenate((data[:,59][882:],data[:,59][441:882]))
#            peak_position = np.concatenate((data[:,60][882:],data[:,60][441:882]))
#            peak_width = np.concatenate((data[:,61][882:],data[:,61][441:882]))    
#            peak_intensity = np.concatenate((data[:,62][882:],data[:,62][441:882]))
# whole ternary
            ROI2 = data[:,16]
            ROI1 = data[:,15]
            ROI3 = data[:,17]
            ROI4 = data[:,18]
            ROI5 = data[:,19]
            ROI6 = data[:,20]
            metal1 = data[:,57]
            metal2 = data[:,58]
            metal3 = data[:,59]
            peak_position = data[:,60]
            peak_width = data[:,61] 
            peak_intensity = data[:,62]
    return ROI1, ROI2, ROI3, ROI4, ROI5, ROI6, metal1, metal2, metal3, peak_position, peak_width, peak_intensity
#    return metal1, metal2, metal3, peak_num
                 
ROI1, ROI2, ROI3, ROI4, ROI5, ROI6, metal1, metal2, metal3, peak_position, peak_width, peak_intensity = twoD_visualize(path)
#plate_x, plate_y, ROI1, ROI2, ROI3, ROI5, crystallinity, texture, metal1, metal2, metal3, peak_num = twoD_visualize(path)

#plt.figure(1)
#plt.plot(metal2, ROI5, 'o')
#m,b = polyfit(ROI5, metal2, 1)
#plt.plot(ROI5*0.0023, ROI5, 'o')

#
#plt.figure(2)
#plt.plot(metal1, ROI2, 'o')
#m,b = polyfit(ROI2, metal1, 1) 
#plt.plot(0.0000856*ROI2, ROI2, 'o')
#plt.xlim(0, 100)
##
ternary_data = np.concatenate(([metal1],[metal2],[metal3],[peak_width]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='peak_width_ternary',
                       cbl='Scale', vmin = 0.13, vmax = 0.406, cmap='jet_r', cb=True, style='h')

labels = []
for pw in peak_width:
    if pw < 0.18:
        label = 3
    elif pw > 0.35:
        label = 1
    else:
        label = 2
    labels.append(label)

ternary_data = np.concatenate(([metal1],[metal2],[metal3],[labels]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='glass_or_crystal',
                       cbl='Scale', vmin = 0.2, vmax = 3.2, cmap='jet', cb=True, style='h')


ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI2]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='ROI2',
                       cbl='Scale', vmin = 772, vmax = 1100000.0, cmap='jet', cb=True, style='h')


ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI1]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='ROI1',
                       cbl='Scale', vmin = 772, vmax = 264000.0, cmap='jet', cb=True, style='h')
                       
ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI3]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='ROI3',
                       cbl='Scale', vmin = 772, vmax = 158000.0, cmap='jet', cb=True, style='h')
                       
ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI4]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='ROI4',
                       cbl='Scale', vmin = 772, vmax = 12000.0, cmap='jet', cb=True, style='h')
                       
ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI5]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='ROI5',
                       cbl='Scale', vmin = 772, vmax = 37900.0, cmap='jet', cb=True, style='h')
                       
ternary_data = np.concatenate(([metal1],[metal2],[metal3],[ROI6]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='ROI6',
                       cbl='Scale', vmin = 772, vmax = 185000.0, cmap='jet', cb=True, style='h')

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

##
#ternary_data = np.concatenate(([metal1],[metal2],[metal3],[peak_num]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='peak_num',
#                       cbl='Scale', vmin = 1, vmax = 14,  cmap='jet', cb=True, style='h')

plt.close("all")

