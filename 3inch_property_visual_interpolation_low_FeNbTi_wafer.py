# -*- coding: utf-8 -*-
"""
Created on Wed July 13 2016

@author: fangren, T Williams
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


path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\FeNbTi\\masterfiles\\'
save_path = path + 'plots\\'

basename1 = 'SampleB2_19_master_metadata.csv'
basename2 = 'SampleB2_20_master_metadata.csv'
basename3 = 'SampleB2_21_master_metadata.csv'

filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)
data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)
data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)

data = data1

ROI1 = data[:, 15]
keep = ROI1>(np.median(ROI1)/5)
data = data[keep,:]

p_x = data[:, 2]
p_y = data[:, 1]
ROI1 = data[:, 15]
Fe = data[:,55]*100
Nb = data[:,56]*100
Ti = data[:,57]*100
peak_position = data[:,52]
peak_width = data[:,53]
peak_intensity = data[:,54]

#
# area = 380
#
# plt.figure(1, figsize = (12, 9))
# plt.title('peak width')
# plt.scatter(p_x, p_y, c = peak_width, s = area, marker = 's')
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.colorbar()
# plt.xlabel('p_x')
# plt.ylabel('p_y(flat)')
# plt.clim(0.1, 0.6)
#

ternary_data = np.concatenate(([Fe],[Nb],[Ti],[peak_width]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Fe','Nb','Ti'), scale=100,
                       sv=True, svpth=save_path, svflnm='peak_width_low',
                       cbl='Scale', vmin = 0.1, vmax = 0.6, cmap='viridis_r', cb=True, style='h')
