# -*- coding: utf-8 -*-
"""
Created on Fri Aug 05 16:31:12 2016

@author: fangren
"""

import numpy as np
import matplotlib.pyplot as plt

def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)

# low power
folder_path = '..//..//..//data//1D_spectra//background_subtracted//'

base_filename1 = 'Sample9_24x24_t30_'
basefile_path1 = folder_path + 'Sample9//'+ base_filename1


base_filename2 = 'Sample10_24x24_t30_'
basefile_path2 = folder_path + 'Sample10//' + base_filename2


base_filename3 = 'Sample18_24x24_t30_'
basefile_path3 = folder_path + 'Sample18//' + base_filename3

save_path = '..//..//figures//'


## making plots
plt.figure(1, figsize = (8, 4))
#################################################################
######################## left panel ###########################
######################## Zr increase ###########################
#################################################################
plt.subplot(131)
indices1 = [74, 73, 72, 71, 88, 87, 86, 103, 102, 101, 119, 118]
indices1.reverse()


indices2 = [74, 73, 92, 112, 133, 132,154, 176, 198]
indices2.reverse()

for index in indices1:
    print 'importing', basefile_path1 + file_index(index) + 'bckgrd_subtracted.csv'
    file_name = basefile_path1 + file_index(index) + 'bckgrd_subtracted.csv'
    spectrum = np.genfromtxt(file_name, delimiter=',', skip_header=0)
    plt.plot(spectrum[:, 0], spectrum[:, 1])

for index in indices2:
    print 'importing', basefile_path2 + file_index(index) + 'bckgrd_subtracted.csv'
    file_name = basefile_path2 + file_index(index) + 'bckgrd_subtracted.csv'
    spectrum = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
    plt.plot(spectrum[:,0],spectrum[:,1])

plt.ylabel('intensity')
plt.plot(spectrum[:,0], [400]*len(spectrum[:,0]), '--r')
plt.plot(spectrum[:,0], [800]*len(spectrum[:,0]), '--r')
plt.xlim((1.5, 4))
plt.ylim((-50, 1100))


#################################################################
######################## middle panel ###########################
######################## Co increase ###########################
#################################################################
plt.subplot(132)

indices1 = [7, 18, 32, 48, 66, 86, 128, 151, 174, 197, 221, 245, 268, 267, 291, 290, 314, 313, 336, 335, 356, 376, 375,
            394, 393, 410, 409, 424, 423, 434,433, 436, 435]


indices2 = [119, 142, 189]


for index in indices2:
    print 'importing', basefile_path2 + file_index(index) + 'bckgrd_subtracted.csv'
    file_name = basefile_path2 + file_index(index) + 'bckgrd_subtracted.csv'
    spectrum = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
    plt.plot(spectrum[:,0],spectrum[:,1])

for index in indices1:
    print 'importing', basefile_path1 + file_index(index) + 'bckgrd_subtracted.csv'
    file_name = basefile_path1 + file_index(index) + 'bckgrd_subtracted.csv'
    spectrum = np.genfromtxt(file_name, delimiter=',', skip_header=0)
    plt.plot(spectrum[:, 0], spectrum[:, 1])




plt.xlabel('Q')
plt.plot(spectrum[:,0], [400]*len(spectrum[:,0]), '--r')
plt.plot(spectrum[:,0], [800]*len(spectrum[:,0]), '--r')
plt.xlim((1.5, 4))
plt.ylim((-50, 1100))
plt.tick_params(axis='both', labelleft='off', labeltop='off', labelright='off')
plt.tight_layout()

#################################################################
######################## right panel ###########################
######################## V increase ###########################
#################################################################
plt.subplot(133)
indices1 = [85, 108, 132, 157, 182, 207]
indices1.reverse()


indices3 = [75, 76, 98, 99, 122, 123, 147, 172, 196, 197, 222, 248, 273, 298, 322, 346]
indices3.reverse()


plt.figure(1, figsize = (4, 6))

for index in indices1:
    print 'importing', basefile_path1 + file_index(index) + 'bckgrd_subtracted.csv'
    file_name = basefile_path1 + file_index(index) + 'bckgrd_subtracted.csv'
    spectrum = np.genfromtxt(file_name, delimiter=',', skip_header=0)
    plt.plot(spectrum[:, 0], spectrum[:, 1])


for index in indices3:
    print 'importing', basefile_path3 + file_index(index) + 'bckgrd_subtracted.csv'
    file_name = basefile_path3 + file_index(index) + 'bckgrd_subtracted.csv'
    spectrum = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
    plt.plot(spectrum[:,0],spectrum[:,1])

plt.plot(spectrum[:,0], [400]*len(spectrum[:,0]), '--r')
plt.plot(spectrum[:,0], [800]*len(spectrum[:,0]), '--r')
plt.xlim((1.5, 4))
plt.ylim((-50, 1100))
plt.tick_params(axis='both', labelleft='off', labeltop='off', labelright='off')

plt.savefig(save_path+'FigureS10d', dpi = 600)