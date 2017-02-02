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


path = 'C:\Research_FangRen\Data\July2016\CoVZr_ternary\masterfiles\high\plotting\\'

def twoD_visualize(path):
    """
    create three lists for plotting: plate_x, plate_y, ROI1, ROI2, ROI3...
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
        if basename(filename)[0] == '1':
            print basename(filename)
            data1 = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            metal1 = data1[:,54]
            metal2 = data1[:,55]
            metal3 = data1[:,56]
            peak_width1 = data1[:,58]
        if basename(filename)[0] == '2':
            print basename(filename)
            data2 = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            peak_width2 = data2[:,58] 

    return metal1, metal2, metal3, peak_width2-peak_width1
                 
           

metal1, metal2, metal3, peak_width_difference = twoD_visualize(path)

area = [500]*len(plate_x)


#plt.figure(1, figsize = (12, 9))
#plt.title('Cobalt beta')
#plt.scatter(plate_y, plate_x, c = ROI3, s = area, marker = 's')
#plt.colorbar()
#plt.xlim((-36, 36))
#plt.ylim((-36, 36))
#plt.xlabel('plate_y')
#plt.ylabel('plate_x(flat)')
#plt.savefig(path+'Cobalt beta.png')
#
#plt.figure(2, figsize = (12, 9))
#plt.title('Chromium alpha Valladium beta')
#plt.scatter(plate_y, plate_x, c = ROI5, s = area, marker = 's')
#plt.colorbar()
#plt.xlim((-36, 36))
#plt.ylim((-36, 36))
#plt.xlabel('plate_y')
#plt.ylabel('plate_x(flat)')
#plt.savefig(path+'Chromium alpha Valladium beta.png')
#
#plt.figure(3, figsize = (12, 9))
#plt.title('Cobalt Iron alpha')
#plt.scatter(plate_y, plate_x, c = ROI2, s = area, marker = 's')
#plt.colorbar()
#plt.xlim((-36, 36))
#plt.ylim((-36, 36))
#plt.xlabel('plate_y')
#plt.ylabel('plate_x(flat)')
#plt.savefig(path+'Cobalt and Iron alpha.png')
#
#
#plt.figure(4, figsize = (12, 9))
#plt.title('Vanadium alpha')
#plt.scatter(plate_y, plate_x, c = ROI1, s = area, marker = 's')
#plt.colorbar()
#plt.xlim((-36, 36))
#plt.ylim((-36, 36))
#plt.xlabel('plate_y')
#plt.ylabel('plate_x(flat)')
##plt.clim((500, 900))
#plt.savefig(path+'Vanadium alpha.png')
#
#plt.figure(5, figsize = (12, 9))
#plt.title('peak position')
#plt.scatter(plate_y, plate_x, c = peak_position, s = area, marker = 's')
#plt.colorbar()
#plt.xlim((-36, 36))
#plt.ylim((-36, 36))
#plt.xlabel('plate_y')
#plt.ylabel('plate_x(flat)')
#plt.savefig(path+'peak position.png')
#
#plt.figure(6, figsize = (12, 9))
#plt.title('peak width')
#plt.scatter(plate_y, plate_x, c = peak_width, s = area, marker = 's')
#plt.colorbar()
#plt.xlim((-36, 36))
#plt.ylim((-36, 36))
#plt.xlabel('plate_y')
#plt.ylabel('plate_x(flat)')
#plt.savefig(path+'peak width.png')
#
#plt.figure(7, figsize = (12, 9))
#plt.title('peak intensity')
#plt.scatter(plate_y, plate_x, c = peak_intensity, s = area, marker = 's')
#plt.colorbar()
#plt.xlim((-36, 36))
#plt.ylim((-36, 36))
#plt.xlabel('plate_y')
#plt.ylabel('plate_x(flat)')
#plt.savefig(path+'peak intensity.png')

ternary_data = np.concatenate(([metal1],[metal2],[metal3],[peak_width_difference]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='peak_width_ternary',
                       cbl='Scale', cmap='jet', cb=True, style='h')



plt.close("all")