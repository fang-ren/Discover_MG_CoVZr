## -*- coding: utf-8 -*-
#"""
#Created on Wed July 13 2016
#
#@author: fangren
#"""


import numpy as np
import matplotlib.pyplot as plt
import imp


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\masterfiles\\high\\'
save_path = path + 'plots\\'

basename1 = 'CLEANED_Sample8_master_metadata_high.csv'
basename2 = 'CLEANED_Sample14_master_metadata_high.csv'
basename3 = 'CLEANED_Sample17_master_metadata_high.csv'

filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)
data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)
data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)

data = np.concatenate((data1, data2, data3[:, :69]))

Co_alpha1 = data[:, 66]
Co_alpha2 = data[:, 67]
Co_beta = data[:, 68]
V_alpha1 = data[:, 63]
V_alpha2 = data[:, 64]
V_beta = data[:, 65]
Co = data[:,57]*100
V = data[:,58]*100
Zr = data[:,59]*100


ternary_data = np.concatenate(([Co],[V],[Zr],[Co_alpha1]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                      sv=True, svpth=save_path, svflnm='Co_alpha1_ternary',
                      cbl='Scale', vmin = 8.23, vmax = 23700.0, cmap='jet', cb=True, style='h')


ternary_data = np.concatenate(([Co],[V],[Zr],[V_alpha1]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='V_alpha1_ternary',
                       cbl='Scale', vmin = 5.84, vmax = 11800, cmap='jet', cb=True, style='h')


plt.close("all")

