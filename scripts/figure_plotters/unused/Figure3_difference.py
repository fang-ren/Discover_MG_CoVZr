# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:34:53 2016

@author: fangren
"""

"""
find indices
"""

import numpy as np
import imp
from scipy import interpolate


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")

path = '..//..//data//master_data//'
save_path = '..//..//figures//'

# high power data


basename1 = 'CLEANED_Sample8_master_metadata_high_WDS.csv'
basename2 = 'CLEANED_Sample14_master_metadata_high.csv'
basename3 = 'CLEANED_Sample17_master_metadata_high_WDS.csv'

filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)
data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)
data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)
data_high = np.concatenate((data1[:, :69], data2[:, :69], data3[:, :69]))

Co_high = data_high[:,57]*100
V_high = data_high[:,58]*100
Zr_high = data_high[:,59]*100
width_high = data_high[:,61]
width_high_neighborhood = np.copy(width_high)

# neighborhood voting
neighborhood_window = 1

for i in range(len(Co_high)):
    for j in range(len(Co_high)):
        if abs(Co_high[i]-Co_high[j]) < neighborhood_window\
        and abs(V_high[i]-V_high[j]) < neighborhood_window\
        and abs(Zr_high[i]-Zr_high[j]) < neighborhood_window:
            peak_width_max = np.max([width_high[i], width_high[j]])
            width_high_neighborhood[i] = peak_width_max
            width_high_neighborhood[j] = peak_width_max
        else:
            continue


# low power data

basename1 = 'CLEANED_Sample9_master_metadata_low.csv'
basename2 = 'CLEANED_Sample10_master_metadata_low.csv'
basename3 = 'CLEANED_Sample18_master_metadata_low.csv'

filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)
data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)
data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)
data_low = np.concatenate((data1[:, :69], data2[:, :69], data3[:, :69]))

Co_low = data_low[:,57]*100
V_low = data_low[:,58]*100
Zr_low = data_low[:,59]*100
width_low = data_low[:,61]
width_low_neighborhood = np.copy(width_low)

# neighborhood voting
neighborhood_window = 1

for i in range(len(Co_low)):
    for j in range(len(Co_low)):
        if abs(Co_low[i]-Co_low[j]) < neighborhood_window\
        and abs(V_low[i]-V_low[j]) < neighborhood_window\
        and abs(Zr_low[i]-Zr_low[j]) < neighborhood_window:
            peak_width_max = np.max([width_low[i], width_low[j]])
            width_low_neighborhood[i] = peak_width_max
            width_low_neighborhood[j] = peak_width_max
        else:
            continue


# interpolate
peak_width_func_high = interpolate.Rbf(Co_high, V_high, Zr_high, width_high_neighborhood, function='multiquadric', smooth=0.3)
peak_width_func_low = interpolate.Rbf(Co_low, V_low, Zr_low, width_low_neighborhood, function='multiquadric', smooth=0.3)


Co_range = np.arange(7.5, 81.7, 1)
V_range = np.arange(8.7, 76.5, 1)

Co_new = []
V_new = []
Zr_new = []

peak_width_new_low = []
peak_width_new_high = []

for i in Co_range:
    for j in V_range:
        if i + j <= 91.5 and i+j >= 29.5:
            try:
                Co_new.append(i)
                V_new.append(j)
                Zr_new.append(100-i-j)
                peak_width_new_high.append(float(peak_width_func_high(i, j, (100-i-j))))
                peak_width_new_low.append(float(peak_width_func_low(i, j, (100-i-j))))
            except(ValueError):
                continue

peak_width_new_low = np.array(peak_width_new_low)
peak_width_new_high = np.array(peak_width_new_high)

#
# ternary_data = np.concatenate(([Co_new],[V_new],[Zr_new],[peak_width_new_high]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                        sv=True, svpth=save_path, svflnm='peak_width_high',
#                        cbl='Scale', vmin = 0.341, vmax = 0.964, cmap='viridis_r', cb=True, style='h')
#
#
# ternary_data = np.concatenate(([Co_new],[V_new],[Zr_new],[peak_width_new_low]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                        sv=True, svpth=save_path, svflnm='peak_width_low',
#                        cbl='Scale', vmin = 0.341, vmax = 0.964, cmap='viridis_r', cb=True, style='h')

width_difference = peak_width_new_low-peak_width_new_high

ternary_data = np.concatenate(([Co_new],[V_new],[Zr_new],[width_difference]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure3e',
                       cbl='FWHM(low-power) - FWHM(high-power)', vmax = 0.27, vmin = 0, cmap='viridis', cb=True, style='h')

print(peak_width_new_high.max(), peak_width_new_high.min())
print(peak_width_new_low.max(), peak_width_new_low.min())
print(width_difference.max(), width_difference.min())
