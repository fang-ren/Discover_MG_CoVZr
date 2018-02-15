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


path = '..//..//data//master_data//'
save_path = '..//..//figures//'

basename = 'CLEANED_Sample15_master_metadata.csv'


filename = path + basename



data = np.genfromtxt(filename, delimiter=',', skip_header = 1)


Co = data[:,57]
V = data[:,58]
Zr = data[:,59]
peak_position = data[:,60]
peak_width = data[:,61]
peak_intensity = data[:,62]
peak_width_neighborhood = np.copy(peak_width)


# ternary_data = np.concatenate(([Co],[V],[Zr],[peak_width]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                        sv=True, svpth=save_path, svflnm='peak_width_thick',
#                        cbl='Scale', vmin = 0.341, vmax = 0.964, cmap='viridis_r', cb=True, style='h')
#
# ternary_data = np.concatenate(([Co],[V],[Zr],[peak_position]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                        sv=True, svpth=save_path, svflnm='peak_position_thick',
#                        cbl='Scale', vmin = 2.51, vmax = 3.14, cmap='viridis', cb=True, style='h')


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
#
#
# ternary_data = np.concatenate(([Co],[V],[Zr],[peak_width_neighborhood]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                        sv=True, svpth=save_path, svflnm='peak_width_neighborhood_high',
#                        cbl='Scale', vmin = 0.341, vmax = 0.964, cmap='viridis_r', cb=True, style='h')
#

# # interpolation
peak_width_func = interpolate.Rbf(Co, V, Zr, peak_width_neighborhood, function='multiquadric', smooth=0.3)


def line(V1, Zr1, V2, Zr2):
    a = (Zr1-Zr2)/(V1-V2)
    b = Zr1-a*V1
    return a, b

left = line(9.0,9.0,20.0,50.0)
right = line(9.0,9.0,50.0,20.0)
bottom = line(30.0, 50.0, 50.0, 30.0)


Co_range = np.arange(1, 100, 1)
V_range = np.arange(1, 100, 1)

Co_new = []
V_new = []
Zr_new = []

peak_width_new = []

for Co in Co_range:
    for V in V_range:
        Zr = 100-Co-V
        if Zr <= left[0]*V + left[1] and Zr >= right[0]*V + right[1] and Zr <= bottom[0]*V + bottom[1] and Zr <= 48 and V <= 50:
        #if Zr >= right[0] * V + right[1]:
            #print 'pass'
            try:
                Co_new.append(Co)
                V_new.append(V)
                Zr_new.append(Zr)
                peak_width_new.append(float(peak_width_func(Co, V, Zr)))
            except(ValueError):
                continue




Co_new = np.array(Co_new)
V_new = np.array(V_new)
Zr_new = np.array(Zr_new)
peak_width_new = np.array(peak_width_new)

# print Co_new.max(), V_new.max(), Zr_new.max()
# print Co_new.min(), V_new.min(), Zr_new.min()

print(peak_width.max(), peak_width.min())
print(peak_width_new.max(), peak_width_new.min())



# ternary_data = np.concatenate(([Co_new],[V_new],[Zr_new],[peak_width_new]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                        sv=True, svpth=save_path, svflnm='peak_width_interpolated_thick',
#                        cbl='Scale', vmin = 0.341, vmax = 0.964, cmap='viridis_r', cb=True, style='h')


labels = []
for pw in peak_width_new:
    if pw < 0.16:
        label = 0
    elif pw > 0.57:
        label = 1
    else:
        label = 0.5
    labels.append(label)


ternary_data = np.concatenate(([Co_new],[V_new],[Zr_new],[labels]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='FigureS3a',
                       cbl='Glass formation', vmax = 1.4, vmin = -0.1, cmap='viridis_r', cb=True, style='h')
#
#
# # plt.close('all')
# #
#
# # labels = []
# # for pw in peak_width:
# #     if pw < 0.16:
# #         label = 0
# #     elif pw > 0.57:
# #         label = 1
# #     else:
# #         label = 0.5
# #     labels.append(label)
# #
# #
# # save_path_2 = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\Theory\\'
# # data = np.concatenate(([Co], [V], [Zr], [peak_width], [labels]))
# # np.savetxt(save_path_2+'peak_width_high.csv', data.T, delimiter=',')
#
#
# print peak_position.max(), peak_position.min()
# print peak_width.max(), peak_width.min()