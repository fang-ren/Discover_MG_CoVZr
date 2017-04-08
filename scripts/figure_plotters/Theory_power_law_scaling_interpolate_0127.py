# -*- coding: utf-8 -*-
"""
Created on Wed July 13 2016

@author: fangren

Implement from paper:
"Power-law scaling and fractal nature of medium-range order in metallic glasses"
D. Ma, et al
Nature Materials
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from os.path import basename
import imp
from scipy import interpolate
from scipy.stats import linregress

plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")

# high power
path = 'C:\\Research_FangRen\\Data\\\Metallic_glasses_data\\CoVZr_ternary\\masterfiles\\high\\'

basename1 = 'CLEANED_Sample8_master_metadata_high_WDS_Travis.csv'
basename2 = 'CLEANED_Sample14_master_metadata_high.csv'
basename3 = 'CLEANED_Sample17_master_metadata_high_WDS.csv'

#
# # low power
# path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoVZr_ternary\\masterfiles\\low\\'
#
# basename1 = 'CLEANED_Sample9_master_metadata_low.csv'
# basename2 = 'CLEANED_Sample10_master_metadata_low.csv'
# basename3 = 'CLEANED_Sample18_master_metadata_low.csv'


##
save_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoVZr_ternary\\Theory\\'

filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)
data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)
data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)

data = np.concatenate((data1[:, :69], data2[:, :69], data3[:, :69]))

Co = data[:,57]*100
V = data[:,58]*100
Zr = data[:,59]*100
peak_position = data[:,60]
peak_width = data[:,61]
peak_width_neighborhood = np.copy(peak_width)
peak_intensity = data[:,62]
peak_position_neighborhood = np.copy(peak_position)

#
# ternary_data = np.concatenate(([Co],[V],[Zr],[peak_position]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                       sv=True, svpth=save_path, svflnm='peak position',
#                       cbl='Scale', cmap='viridis', cb=True, style='h')

# neighborhood voting
neighborhood_window = 1

for i in range(len(Co)):
    for j in range(len(Co)):
        if abs(Co[i]-Co[j]) < neighborhood_window\
        and abs(V[i]-V[j]) < neighborhood_window\
        and abs(Zr[i]-Zr[j]) < neighborhood_window:
            peak_width_ave = np.average([peak_width[i], peak_width[j]])
            peak_width_min = np.min([peak_width[i], peak_width[j]])
            peak_width_max = np.max([peak_width[i], peak_width[j]])
            peak_width_neighborhood[i] = peak_width_max
            peak_width_neighborhood[j] = peak_width_max
        else:
            continue

for i in range(len(Co)):
    for j in range(len(Co)):
        if abs(Co[i]-Co[j]) < neighborhood_window\
        and abs(V[i]-V[j]) < neighborhood_window\
        and abs(Zr[i]-Zr[j]) < neighborhood_window:
            peak_position_ave = np.average([peak_position[i], peak_position[j]])
            peak_position_min = np.min([peak_position[i], peak_position[j]])
            peak_position_max = np.max([peak_position[i], peak_position[j]])
            peak_position_neighborhood[i] = peak_position_max
            peak_position_neighborhood[j] = peak_position_max
        else:
            continue
#
# ternary_data = np.concatenate(([Co], [V], [Zr], [peak_position_neighborhood]), axis=0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('Co', 'V', 'Zr'), scale=100,
#                              sv=True, svpth=save_path, svflnm='peak position neighborhood',
#                              cbl='Scale', cmap='viridis', cb=True, style='h')

# interpolation
peak_position_func = interpolate.Rbf(Co, V, Zr, peak_position, function='multiquadric', smooth=0.3)
peak_width_func = interpolate.Rbf(Co, V, Zr, peak_width_neighborhood, function='multiquadric', smooth=0.3)


# # high power
# Co_range = np.arange(4.4, 82.4, 1)
# V_range = np.arange(8, 80.0, 1)
#
#
# Co_new = []
# V_new = []
# Zr_new = []
#
# peak_position_new = []
# peak_width_new = []
#
# for i in Co_range:
#     for j in V_range:
#         if i + j <= 92.3 and i+j >= 24.4:
#             try:
#                 Co_new.append(i)
#                 V_new.append(j)
#                 Zr_new.append(100-i-j)
#                 peak_position_new.append(float(peak_position_func(i, j, (100-i-j))))
#                 peak_width_new.append(float(peak_width_func(i, j, (100-i-j))))
#             except(ValueError):
#                 continue


# low power
Co_range = np.arange(7.5, 81.7, 1)
V_range = np.arange(8.7, 76.5, 1)

Co_new = []
V_new = []
Zr_new = []

peak_position_new = []
peak_width_new = []

for i in Co_range:
    for j in V_range:
        if i + j <= 91.5 and i+j >= 29.5:
            try:
                Co_new.append(i)
                V_new.append(j)
                Zr_new.append(100-i-j)
                peak_position_new.append(float(peak_position_func(i, j, (100-i-j))))
                peak_width_new.append(float(peak_width_func(i, j, (100 - i - j))))
            except(ValueError):
                continue

#####################################

Co_new = np.array(Co_new)
V_new = np.array(V_new)
Zr_new = np.array(Zr_new)
peak_position_new = np.array(peak_position_new)
peak_width_new = np.array(peak_width_new)


MG = peak_width_new >= 0.57
#
#
# ternary_data = np.concatenate(([Co_new], [V_new], [Zr_new], [peak_position_new]), axis=0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('Co', 'V', 'Zr'), scale=100,
#                              sv=True, svpth=save_path, svflnm='peak position interpolate',
#                              cbl='Scale', cmap='viridis', cb=True, style='h')
#

Co_c = Co_new/100
V_c = V_new/100
Zr_c = Zr_new/100

Co = Co_c * 100
V = V_c * 100
Zr = Zr_c * 100

# # calculatin is shown in a separate word file
# Co_volume = 11.025
# V_volume = 14.74
# Zr_volume = 24.66

f = 1
Co_volume = 11.05*f
V_volume = 15.38*f
Zr_volume = 26.11*f

atomic_volume = Co_c * Co_volume + V_c * V_volume + Zr_c * Zr_volume

# # plot peak position Vs atomic volume
# plt.figure(1)
# plt.title('all data, low power')
# plt.plot(atomic_volume, peak_position_new, 'o')
# plt.xlabel('Atomic Volume')
# plt.ylabel('FSDP')
# plt.xscale('log')
# plt.yscale('log')
# plt.xlim(12, 22)
# plt.ylim(2.4, 3.2)
# plt.ylim()
# plt.savefig(save_path + 'V-q_all_low_power')


scale1 = peak_position_new * (atomic_volume ** 0.426)
scale2 = peak_position_new * (atomic_volume ** 0.44)
#
# #ternary_data = np.concatenate(([Co],[V],[Zr],[atomic_volume]), axis = 0)
# #ternary_data = np.transpose(ternary_data)
# #
# #plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
# #                       sv=True, svpth=path, svflnm='atomic volume',
# #                       cbl='Scale', cmap='jet_r', cb=True, style='h')
#
# #
# # ternary_data = np.concatenate(([Co_new],[V_new],[Zr_new],[scale]), axis = 0)
# # ternary_data = np.transpose(ternary_data)
# #
# # plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
# #                        sv=True, svpth=save_path, svflnm='power_scaling',
# #                        cbl='Scale', cmap='jet_r', cb=True, style='h')
#
quasicrystals = (np.abs(scale1 - 9.3) < 0.2)+(np.abs(scale2 - 9.3) < 0.2)

ternary_data = np.concatenate(([Co_new],[V_new],[Zr_new],[quasicrystals]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='quasicrystals',
                       cbl='Scale', vmax = 1.4, vmin = -0.1, cmap='viridis_r', cb=True, style='h')

# np.savetxt(save_path+'quasicrystals.csv', ternary_data, delimiter=',')

# # plot peak position Vs atomic volume
# plt.figure(2)
# plt.title('quasicrystals, low power')
# plt.plot(np.log(atomic_volume[MG]), np.log(peak_position_new[MG]), 'o')
# slope, intercept, r_value, p_value, std_err = linregress(np.log(atomic_volume[MG]), np.log(peak_position_new[MG]))
# plt.plot(np.log(atomic_volume[MG]), -0.44*np.log(atomic_volume[MG])+np.log(9.1), 'r--')
# plt.plot(np.log(atomic_volume[MG]), -0.44*np.log(atomic_volume[MG])+np.log(9.5), 'r--')
# plt.plot(np.log(atomic_volume[MG]), -0.426*np.log(atomic_volume[MG])+np.log(9.1), 'r--')
# plt.plot(np.log(atomic_volume[MG]), -0.426*np.log(atomic_volume[MG])+np.log(9.5), 'r--')

# # plt.plot(np.log(atomic_volume), -0.44*np.log(atomic_volume)+np.log(9.1), 'r--')
# # plt.plot(np.log(atomic_volume), -0.44*np.log(atomic_volume)+np.log(9.5), 'r--')
# # plt.plot(np.log(atomic_volume), -0.426*np.log(atomic_volume)+np.log(9.1), 'r--')
# # plt.plot(np.log(atomic_volume), -0.426*np.log(atomic_volume)+np.log(9.5), 'r--')
# plt.xlabel('log(Atomic Volume)')
# plt.ylabel('log(FSDP)')
# # plt.xlim(12, 22)
# # plt.ylim(2.4, 3.2)
# plt.savefig(save_path + 'V-q_quasicrystals_low_power')
# # plt.close('all')