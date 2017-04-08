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


path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoVZr_ternary\\masterfiles\\Comparing _thickness\\'
save_path = path + 'plots\\'

basename1 = 'Sample15_master_metadata.csv'
basename2 = 'Sample14_master_metadata.csv'

filename1 = path + basename1
filename2 = path + basename2


data = np.genfromtxt(filename1, delimiter=',', skip_header = 1)

plate_x = data[:,1]
plate_y = data[:,2]
Co = data[:,57]
V = data[:,58]
Zr = data[:,59]
peak_position = data[:,60]
peak_width = data[:,61]
peak_intensity = data[:,62]


labels = []
for pw in peak_width:
    if pw < 0.16:
        label = 0
    elif pw > 0.57:
        label = 1
    else:
        label = 0.5
    labels.append(label)

area = 300

plt.figure(4, figsize = (12, 9))
plt.scatter(plate_y, plate_x, c = labels, s = area, marker = 's')
plt.colorbar()
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')




