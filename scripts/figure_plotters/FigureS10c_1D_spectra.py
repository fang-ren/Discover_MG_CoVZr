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


# high power
folder_path = '..//..//..//data//1D_spectra//background_subtracted//'


base_filename1 = 'Sample8_24x24_t30_'
basefile_path1 = folder_path + 'Sample8//' + base_filename1


base_filename2 = 'Sample14_7thin_24x24_t30_'
basefile_path2 = folder_path + 'Sample14//' + base_filename2


base_filename3 = 'Sample17_24x24_t30_'
basefile_path3 = folder_path + 'Sample17//' + base_filename3

save_path = '..//..//figures//'


## making plots
plt.figure(1, figsize = (8, 4))
#################################################################
######################## left panel ###########################
######################## Zr increase ###########################
#################################################################
plt.subplot(131)
indices1 = [207, 231, 230, 229, 228, 227, 226, 246, 245, 244, 243, 262, 261, 260]
indices1.reverse()

indices3 = [366, 383, 398, 411]
indices3.reverse()

for index in indices3:
    print 'importing', basefile_path3 + file_index(index) + 'bckgrd_subtracted.csv'
    file_name = basefile_path3 + file_index(index) + 'bckgrd_subtracted.csv'
    spectrum = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
    plt.plot(spectrum[:,0],spectrum[:,1])

for index in indices1:
    print 'importing', basefile_path1 + file_index(index) + 'bckgrd_subtracted.csv'
    file_name = basefile_path1 + file_index(index) + 'bckgrd_subtracted.csv'
    spectrum = np.genfromtxt(file_name, delimiter=',', skip_header=0)
    plt.plot(spectrum[:, 0], spectrum[:, 1])

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

indices1 = [11, 58, 78, 120, 143, 166, 212, 236]

indices2 = [107, 129, 152, 175, 198, 222, 246, 269, 292, 315, 337, 358, 359, 378, 379, 396, 397, 412, 413, 425, 426, 427, 436, 437, 438, 439]

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
indices1 = [257, 282, 283, 308, 332, 355, 398, 416, 418]
indices1.reverse()


indices3 = [235, 236, 261, 262, 263, 264, 265, 291, 292, 293, 320, 321]
indices3.reverse()


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

plt.savefig(save_path+'FigureS10c', dpi = 600)