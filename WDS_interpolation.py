# -*- coding: utf-8 -*-
"""
Created on Wed July 13 2016

@author: fangren

"""

import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from os.path import basename
import imp
from scipy import interpolate



path = 'C:\\Research_FangRen\Data\\July2016\\CoVZr_ternary\\XRF\\WDS\\sample_8\\'

save_path = path



for filename in glob.glob(os.path.join(path, '*.csv')):
    if basename(filename)[0] == 'W':
        print basename(filename)
        data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
        plate_x_177 = data[:,4]
        plate_y_177 = data[:,5]
        Co_177 = data[:,3]
        V_177 = data[:,2]
        Zr_177 = data[:,1]
    elif basename(filename)[0] == '4':
        print basename(filename)
        data = np.genfromtxt(filename, delimiter=',', skip_header=1)
        plate_x_441 = data[:, 0]
        plate_y_441 = data[:, 1]

func_Co = interpolate.SmoothBivariateSpline(plate_x_177, plate_y_177, Co_177, kx = 3, ky = 3)
func_V = interpolate.SmoothBivariateSpline(plate_x_177, plate_y_177, V_177, kx = 3, ky = 3)
func_Zr = interpolate.SmoothBivariateSpline(plate_x_177, plate_y_177, Zr_177, kx = 3, ky = 3)

Co_441 = []
V_441 = []
Zr_441 = []

for i in range(len(plate_x_441)):
    Co_441.append(func_Co(plate_x_441[i], plate_y_441[i]))
    V_441.append(func_V(plate_x_441[i], plate_y_441[i]))
    Zr_441.append(func_Zr(plate_x_441[i], plate_y_441[i]))


data_interpolate = np.concatenate((Co_441, V_441, Zr_441), axis = 1)

np.savetxt(path+'new_WDS_441.csv', data_interpolate, delimiter= ',')


area_177 = 1100

area_441 = 450

plt.figure(1, figsize = (12, 9))
plt.title('Co_177')
plt.scatter(plate_y_177, plate_x_177, c = Co_177, s = area_177, marker = 's')
plt.colorbar()
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.clim(5.98, 55.56)
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.savefig(path+'Co_177')


plt.figure(2, figsize = (12, 9))
plt.title('V_177')
plt.scatter(plate_y_177, plate_x_177, c = V_177, s = area_177, marker = 's')
plt.colorbar()
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.clim(13.08, 48.07)
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.savefig(path+'V_177')

plt.figure(3, figsize = (12, 9))
plt.title('Zr_177')
plt.scatter(plate_y_177, plate_x_177, c = Zr_177, s = area_177, marker = 's')
plt.colorbar()
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.clim(28.29, 74.92)
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.savefig(path+'Zr_177')

plt.figure(4, figsize = (12, 9))
plt.title('Co_441')
plt.scatter(plate_y_441, plate_x_441, c = Co_441, s = area_441, marker = 's')
plt.colorbar()
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.clim(5.98, 55.56)
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.savefig(path+'Co_441')

plt.figure(5, figsize = (12, 9))
plt.title('V_441')
plt.scatter(plate_y_441, plate_x_441, c = V_441, s = area_441, marker = 's')
plt.colorbar()
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.clim(13.08, 48.07)
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.savefig(path+'V_441')

plt.figure(6, figsize = (12, 9))
plt.title('Zr_441')
plt.scatter(plate_y_441, plate_x_441, c = Zr_441, s = area_441, marker = 's')
plt.colorbar()
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.clim(28.29, 74.92)
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.savefig(path+'Zr_441')

plt.close('all')