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

data = np.concatenate((data1, data2, data3))

ROI1 = data[:, 15]
keep = ROI1>(np.median(ROI1)/5)
data = data[keep,:]



plate_y = data[:,1]
plate_x = data[:,2]
ROI1 = data[:,15]
ROI2 = data[:,16]
ROI3 = data[:,17]
ROI4 = data[:,18]
ROI5 = data[:,19]
ROI6 = data[:,20]
Fe = data[:,55] * 100
Nb = data[:,56] * 100
Ti = data[:,57] * 100
Ti_alpha = data[:,61]
Ti_beta = data[:, 62]
Fe_alpha = data[:, 63]
Fe_beta = data[:, 64]

area = 460
# area = 300

#
# plt.figure(1, figsize = (12, 9))
# plt.title('ROI1')
# plt.scatter(plate_y, plate_x, c = ROI1, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_y')
# plt.ylabel('plate_x(flat)')
# #plt.savefig(path+'ROI1.png')
#
# plt.figure(2, figsize = (12, 9))
# plt.title('ROI2')
# plt.scatter(plate_y, plate_x, c = ROI2, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_y')
# plt.ylabel('plate_x(flat)')
# #plt.savefig(path+'ROI2.png')
#
# plt.figure(3, figsize = (12, 9))
# plt.title('ROI3')
# plt.scatter(plate_y, plate_x, c = ROI3, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_y')
# plt.ylabel('plate_x(flat)')
# #plt.savefig(path+'ROI3.png')
#
# plt.figure(4, figsize = (12, 9))
# plt.title('ROI4')
# plt.scatter(plate_y, plate_x, c = ROI4, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_y')
# plt.ylabel('plate_x(flat)')
# #plt.savefig(path+'ROI4.png')

# plt.figure(5, figsize = (12, 9))
# plt.title('ROI5')
# plt.scatter(plate_y, plate_x, c = ROI5, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-44, 44))
# plt.ylim((-44, 44))
# plt.xlabel('x')
# plt.ylabel('y')
# #plt.savefig(path+'ROI5.png', dpi = 600)

# plt.figure(6, figsize = (12, 9))
# plt.title('ROI6')
# plt.scatter(plate_y, plate_x, c = ROI6, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_y')
# plt.ylabel('plate_x(flat)')
# #plt.savefig(path+'ROI6.png')

#
# plt.figure(7, figsize = (12, 9))
# plt.title('Ti_alpha')
# plt.scatter(plate_x, plate_y, c = Ti_alpha, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_x')
# plt.ylabel('plate_y(flat)')
# # plt.savefig(path+'Co_alpha.png')

# plt.figure(8, figsize = (12, 9))
# plt.title('Ti_beta')
# plt.scatter(plate_x, plate_y, c = Ti_beta, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_x')
# plt.ylabel('plate_y(flat)')
# # plt.savefig(path+'Co_alpha.png')
#
#
# plt.figure(9, figsize = (12, 9))
# plt.title('Fe_alpha')
# plt.scatter(plate_x, plate_y, c = Fe_alpha, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_x')
# plt.ylabel('plate_y(flat)')
# # plt.savefig(path+'Co_alpha.png')


# plt.figure(10, figsize = (12, 9))
# plt.title('Fe_beta')
# plt.scatter(plate_x, plate_y, c = Fe_beta, s = area, marker = 's')
# plt.colorbar()
# plt.xlim((-36, 36))
# plt.ylim((-36, 36))
# plt.xlabel('plate_x')
# plt.ylabel('plate_y(flat)')
# # plt.savefig(path+'Co_alpha.png')


ternary_data = np.concatenate(([Fe],[Nb],[Ti],[Ti_alpha]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Fe','Nb','Ti'), scale=100,
                       sv=True, svpth=save_path, svflnm='Ti alpha',
                       cbl='Scale', cmap='viridis_r', cb=True, style='h')


ternary_data = np.concatenate(([Fe],[Nb],[Ti],[Fe_alpha]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Fe','Nb','Ti'), scale=100,
                       sv=True, svpth=save_path, svflnm='Fe alpha',
                       cbl='Scale', cmap='viridis_r', cb=True, style='h')


plt.close("all")

