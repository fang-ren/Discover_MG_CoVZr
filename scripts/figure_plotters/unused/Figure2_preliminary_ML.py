# -*- coding: utf-8 -*-
"""
Created on Wed July 13 2016

@author: fangren
"""


import numpy as np
import matplotlib.pyplot as plt
import imp
from scipy import interpolate

plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = '..//..//data//ML_prediction//'
save_path = '..//..//figures//'



filename_new = path + 'old-model_Co VZr.csv'
data = np.genfromtxt(filename_new, delimiter=',', skip_header = 1)

Co = data[:,3]*100
V = data[:,4]*100
Zr = data[:,5]*100
probability = data[:, 1]

#
# ternary_data = np.concatenate(([Co],[V],[Zr],[probability]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co', 'V', 'Zr'), scale=100,
#                        sv=True, svpth=save_path, svflnm= 'CoVZr_old_model.png',
#                        cbl='Probability (GFA = True)', vmin = 0.5, vmax = 1, cmap='viridis_r', cb=True, style='h')


# interpolation
probability_func_old = interpolate.Rbf(Co, V, Zr, probability, function='multiquadric',
                                       smooth=0.3)




metal1_range = np.arange(0, 100, 1.5)
metal2_range = np.arange(0, 100, 1.5)

metal1 = []
metal2 = []
metal3 = []

probability_interpolate_old = []
probability_interpolate_new = []

for i in metal1_range:
    for j in metal2_range:
        if i + j <= 100 and i+j >= 0:
            try:
                metal1.append(i)
                metal2.append(j)
                metal3.append(100-i-j)
                probability_interpolate_old.append(float(probability_func_old(i, j, (100-i-j))))
            except(ValueError):
                continue


ternary_data = np.concatenate(([metal1],[metal2],[metal3],[probability_interpolate_old]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co', 'V', 'Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure2.png',
                       cbl='Probability (GFA = True)', vmin = 0.5, vmax = 1, cmap='viridis_r', cb=True, style='h')


plt.close("all")


