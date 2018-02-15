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


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\masterfiles\\high\\plotting\\'

def twoD_visualize(path):
    """
    create three lists for plotting: plate_x, plate_y, ROI1, ROI2, ROI3...
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
        # if basename(filename)[0] == 'P':
            print(basename(filename))
            data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            plate_x = data[:,1]
            plate_y = data[:,2]
            Co_alpha1 = data[:,66]
            Co_alpha2 = data[:,67]
            Co_beta = data[:,68]
            V_alpha1 = data[:,63]
            V_alpha2 = data[:,64]
            V_beta = data[:,65]
            Co_WDS = data[:,69]
            V_WDS = data[:,70]
            Zr_WDS = data[:, 71]
    return plate_x, plate_y, Co_alpha1, Co_alpha2, Co_beta, V_alpha1, V_alpha2, V_beta, Co_WDS, V_WDS, Zr_WDS

                 
plate_x, plate_y, Co_alpha1, Co_alpha2, Co_beta, V_alpha1, V_alpha2, V_beta, Co_WDS, V_WDS, Zr_WDS = twoD_visualize(path)

area = 380

#
# plt.figure(2, figsize = (12, 9))
# plt.title('Co WDS result')
# plt.scatter(plate_y, plate_x, c = Co_WDS, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_y')
# plt.ylabel('plate_x(flat)')
# plt.savefig(path+'Co_WDS.png')
#
# plt.figure(3, figsize = (12, 9))
# plt.title('V WDS result')
# plt.scatter(plate_y, plate_x, c = V_WDS, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_y')
# plt.ylabel('plate_x(flat)')
# plt.savefig(path+'V_WDS.png')
#
# plt.figure(4, figsize = (12, 9))
# plt.title('Zr WDS result')
# plt.scatter(plate_y, plate_x, c = Zr_WDS, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_y')
# plt.ylabel('plate_x(flat)')
# plt.savefig(path+'Zr_WDS.png')

plt.figure(4, figsize = (12, 9))
plt.title('Co XRF result')
plt.scatter(plate_y, plate_x, c = Co_alpha1, s = area, marker = 's')
plt.colorbar()
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.savefig(path+'Co_alpha1.png')

plt.close("all")

