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

basename1 = 'CLEANED_SampleB2_19_master_metadata.csv'
basename2 = 'CLEANED_SampleB2_20_master_metadata.csv'
basename3 = 'CLEANED_SampleB2_21_master_metadata.csv'

filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)
data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)
data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)

data = np.concatenate((data1, data2, data3))
data = data3
# data = np.concatenate((data1[:, :58], data3[:, :58]))

ROI1 = data[:, 15]
p_x = data[:, 2]
p_y = data[:, 1]
Fe = data[:,58]*100
Nb = data[:,59]*100
Ti = data[:,60]*100
peak_position = data[:,52]
peak_width = data[:,53]
peak_intensity = data[:,54]

area = 380

plt.figure(1, figsize = (12, 9))
plt.title('peak width')
plt.scatter(p_x, p_y, c = peak_width, s = area, marker = 's')
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.colorbar()
plt.xlabel('p_x')
plt.ylabel('p_y(flat)')
plt.clim(0.1, 0.6)


