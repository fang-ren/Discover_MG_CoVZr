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
from plotTernary import plt_ternary_save

path = '..//..//data//FeTiNb//master_data//'
save_path = '..//..//figures//'


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
# data = np.concatenate((data1[:, :58], data3[:, :58]))

ROI1 = data[:, 15]
Fe = data[:,58]*100
Ti = data[:,60]*100
Nb = data[:,59]*100
peak_position = data[:,52]
peak_width = data[:,53]
peak_intensity = data[:,54]


peak_width_neighborhood = np.copy(peak_width)


# neighborhood voting
neighborhood_window = 1


for i in range(len(Fe)):
    for j in range(len(Fe)):
        if abs(Fe[i]-Fe[j]) < neighborhood_window\
        and abs(Nb[i]-Nb[j]) < neighborhood_window\
        and abs(Ti[i]-Ti[j]) < neighborhood_window:
            peak_width_ave = np.average([peak_width[i], peak_width[j]])
            peak_width_min = np.min([peak_width[i], peak_width[j]])
            peak_width_max = np.max([peak_width[i], peak_width[j]])
            peak_width_neighborhood[i] = peak_width_max
            peak_width_neighborhood[j] = peak_width_max
        else:
            continue



peak_width_func = interpolate.Rbf(Fe, Nb, Ti, peak_width_neighborhood, function='multiquadric', smooth=0.3)

Fe_range = np.arange(5.8, 84.7, 1)
Nb_range = np.arange(7.3, 78.9, 1)


Fe_new = []
Nb_new = []
Ti_new = []

peak_width_new = []

for i in Fe_range:
    for j in Nb_range:
        if i + j <= 93.5 and i+j >= 23.7:
            try:
                Fe_new.append(i)
                Nb_new.append(j)
                Ti_new.append(100-i-j)
                peak_width_new.append(float(peak_width_func(i, j, (100-i-j))))
            except(ValueError):
                continue


Fe_new = np.array(Fe_new)
Nb_new = np.array(Nb_new)
Ti_new = np.array(Ti_new)
peak_width_new = np.array(peak_width_new)

print peak_width.max(), peak_width.min()
print peak_width_new.max(), peak_width_new.min()



labels = []
for pw in peak_width_new:
    # if pw < 0.16:
    #     label = 0
    if pw < 0.57:
         label = 0
    elif pw >= 0.57:
        label = 1
    # else:
    #     label = 0.5
    labels.append(label)


ternary_data = np.concatenate(([Fe_new],[Ti_new],[Nb_new],[labels]), axis = 0)
ternary_data = np.transpose(ternary_data)

plt_ternary_save(ternary_data, tertitle='',  labelNames=('Fe','Ti','Nb'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure5c',
                       cbl='Scale', vmax = 1, vmin = 0.1, cmap='viridis_r', cb=True, style='h')


plt.close('all')


# labels = []
# for pw in peak_width:
#     if pw < 0.16:
#         label = 0
#     elif pw > 0.57:
#         label = 1
#     else:
#         label = 0.5
#     labels.append(label)
#
#
# save_path_2 = 'C:\\Research_FangRen\\Data\\July2016\\FeNbTi_ternary\\Theory\\'
# data = np.concatenate(([Fe], [Nb], [Ti], [peak_width], [labels]))
# np.savetxt(save_path_2+'peak_width_low.csv', data.T, delimiter=',')


print peak_position.max(), peak_position.min()
print peak_width.max(), peak_width.min()
