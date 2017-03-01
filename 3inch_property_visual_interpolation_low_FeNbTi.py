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

data = np.concatenate((data1[:, :58], data2[:, :58], data3[:, :58]))
ROI1 = data[:, 15]
keep = ROI1>(np.median(ROI1)/10)
data = data[keep,:]

ROI1 = data[:, 15]
Fe = data[:,55]*100
Nb = data[:,56]*100
Ti = data[:,57]*100
peak_position = data[:,52]
peak_width = data[:,53]
peak_intensity = data[:,54]


peak_width_neighborhood = np.copy(peak_width)


ternary_data = np.concatenate(([Fe],[Nb],[Ti],[peak_width]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Fe','Nb','Ti'), scale=100,
                       sv=True, svpth=save_path, svflnm='peak_width_low',
                       cbl='Scale', vmin = 0.341, vmax = 0.964, cmap='viridis_r', cb=True, style='h')

ternary_data = np.concatenate(([Fe],[Nb],[Ti],[peak_position]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Fe','Nb','Ti'), scale=100,
                       sv=True, svpth=save_path, svflnm='peak_position_low',
                       cbl='Scale', vmin = 2.68, vmax = 3.05, cmap='viridis', cb=True, style='h')


ternary_data = np.concatenate(([Fe],[Nb],[Ti],[[1]*len(Fe)]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Fe','Nb','Ti'), scale=100,
                       sv=True, svpth=save_path, svflnm='black_low',
                       cbl='Scale', cmap='gray', cb=True, style='h')




ternary_data = np.concatenate(([Fe],[Nb],[Ti],[ROI1]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Fe','Nb','Ti'), scale=100,
                       sv=True, svpth=save_path, svflnm='ROI1',
                       cbl='Scale', cmap='viridis', cb=True, style='h')


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


ternary_data = np.concatenate(([Fe],[Nb],[Ti],[peak_width_neighborhood]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Fe','Nb','Ti'), scale=100,
                       sv=True, svpth=save_path, svflnm='peak_width_neighborhood_low',
                       cbl='Scale', vmin = 0.341, vmax = 0.964, cmap='viridis_r', cb=True, style='h')


# interpolation
peak_width_func = interpolate.Rbf(Fe, Nb, Ti, peak_width_neighborhood, function='multiquadric', smooth=0.3)

Fe_range = np.arange(7.5, 81.7, 1)
Nb_range = np.arange(8.7, 76.5, 1)


Fe_new = []
Nb_new = []
Ti_new = []

peak_width_new = []

for i in Fe_range:
    for j in Nb_range:
        if i + j <= 91.5 and i+j >= 29.5:
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


ternary_data = np.concatenate(([Fe_new],[Nb_new],[Ti_new],[peak_width_new]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Fe','Nb','Ti'), scale=100,
                       sv=True, svpth=save_path, svflnm='peak_width_interpolated_low',
                       cbl='Scale', vmin = 0.341, vmax = 0.964, cmap='viridis_r', cb=True, style='h')


labels = []
for pw in peak_width_new:
    if pw < 0.16:
        label = 0
    elif pw > 0.57:
        label = 1
    else:
        label = 0.5
    labels.append(label)


ternary_data = np.concatenate(([Fe_new],[Nb_new],[Ti_new],[labels]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Fe','Nb','Ti'), scale=100,
                       sv=True, svpth=save_path, svflnm='glass_or_crystal_low',
                       cbl='Scale', vmax = 1.4, vmin = -0.1, cmap='viridis_r', cb=True, style='h')


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
