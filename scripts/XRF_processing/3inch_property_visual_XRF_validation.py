## -*- coding: utf-8 -*-
#"""
#Created on Wed July 13 2016
#
#@author: fangren
#"""


import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from os.path import basename
import imp
from scipy import polyfit


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\masterfiles\\low\\plotting\\'

def twoD_visualize(path):
    """
    create three lists for plotting: plate_x, plate_y, ROI1, ROI2, ROI3...
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
        if basename(filename)[0] == 'C':
            print(basename(filename))
            data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            Co_model = data[:,57]*100
            V_model = data[:,58]*100
            Zr_model = data[:,59]*100
            Co_alpha1 = data[:,66]
            Co_alpha2 = data[:,67]
            Co_beta = data[:,68]
            V_alpha1 = data[:,63]
            V_alpha2 = data[:,64]
            V_beta = data[:,65]
            Co_WDS = data[:,69]
            V_WDS = data[:,70]
            Zr_WDS = data[:,71]
    return Co_model, V_model, Zr_model, Co_alpha1, Co_alpha2, Co_beta, V_alpha1, V_alpha2, V_beta, Co_WDS, V_WDS, Zr_WDS


Co_model, V_model, Zr_model, Co_alpha1, Co_alpha2, Co_beta, V_alpha1, V_alpha2, V_beta, Co_WDS, V_WDS, Zr_WDS = twoD_visualize(path)

plt.figure(1)
plt.title('Co WDS Vs Co XRF')
plt.xlabel('Co_WDS')
plt.ylabel('Co_alpha1')
plt.plot(Co_WDS, Co_alpha1, 'o')
plt.savefig(path+'Co WDS Vs Co XRF')

plt.figure(2)
plt.title('V WDS Vs V XRF')
plt.xlabel('V_WDS')
plt.ylabel('V_alpha1')
plt.plot(V_WDS, V_alpha1, 'o')
plt.savefig(path+'V WDS Vs V XRF')

plt.figure(3)
plt.title('Co model Vs Co XRF')
plt.xlabel('Co_model')
plt.ylabel('Co_alpha1')
plt.plot(Co_model, Co_alpha1, 'o')
plt.savefig(path+'Co model Vs Co XRF')

plt.figure(4)
plt.title('V model Vs V XRF')
plt.xlabel('V_model')
plt.ylabel('V_alpha1')
plt.plot(V_model, V_alpha1, 'o')
plt.savefig(path+'V model Vs V XRF')


plt.figure(5)
plt.title('Co model Vs Co WDS')
plt.xlabel('Co_model')
plt.ylabel('Co_WDS')
plt.plot(Co_model, Co_WDS, 'o')
plt.savefig(path+'Co model Vs Co WDS')

plt.figure(6)
plt.title('V model Vs V WDS')
plt.xlabel('V_model')
plt.ylabel('V_WDS')
plt.plot(V_model, V_WDS, 'o')
plt.savefig(path+'V model Vs V WDS')


WDS = [1] *len(Co_WDS)
model = [0] * len(Co_WDS)

ternary_data = np.concatenate(([Co_WDS],[V_WDS],[Zr_WDS],[WDS]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='WDS_ternary',
                       cbl='Scale', vmin = 0, vmax = 1, cmap='jet', cb=True, style='h')

ternary_data = np.concatenate(([Co_model],[V_model],[Zr_model],[model]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=path, svflnm='model_ternary',
                       cbl='Scale',  vmin = 0, vmax = 1, cmap='jet', cb=True, style='h')

plt.close('all')
