# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 16:22:25 2016

@author: fangren
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep
import os
import csv



def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)



def read_1D(filename):
    data = np.genfromtxt(filename, delimiter=',', skip_header = 0)
    Qlist = data[:,0][8:937]
    IntAve = data[:,1][3:][8:937]
    return Qlist, IntAve



def select_bckgrd(background_indices):
    background_x = Qlist[background_indices]
    background_y = IntAve[background_indices]
    return background_x, background_y

def save_results(background_x, background_y, Qlist, IntAve, index, base_filename):
    indices = range(1, 930)
    plt.figure(1)
    plt.subplot(311)
    plt.plot(indices, IntAve)
    plt.plot(background_indices, background_y, 'o')
    
    tck = splrep(background_x,background_y)
    
    background = splev(Qlist, tck)
    
    plt.subplot(312)
    plt.plot(Qlist, IntAve)
    plt.plot(Qlist, background)
    plt.plot(background_x, background_y, 'o')
    
    
    plt.subplot(313)
    plt.plot(Qlist, (IntAve-background))
    plt.plot(Qlist, [0]*929, 'r--')
    plt.savefig(save_path + base_filename + file_index(index) + 'bckgrd_subtract.png' )    
    
    plt.close('all')
    
    rows = zip(Qlist, (IntAve-background))
    with open(save_path + base_filename + file_index(index) + 'bckgrd_subtracted.csv', 'a') as csvoutput:
        writer = csv.writer(csvoutput, delimiter = ',', lineterminator = '\n')
        for row in rows:
            writer.writerow(row)
        csvoutput.close()


background_indices = [8, 80, 150, 198, 340, 550, 590, 650, 690, 750, 790, 842, 892, 928]
folder_path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\1Dfiles\\low_power_9_10_18\\'
base_filename1 = 'Sample9_24x24_t30_'
#base_filename2 = 'Sample14_7thin_24x24_t30_'
#base_filename3 = 'Sample17_24x24_t30_'
base_filenames = [base_filename1]

save_path = folder_path + 'background_subtracted_9_correction\\'
if not os.path.exists(save_path):
    os.makedirs(save_path)

indices = [210, 211, 212]
indices += range(234, 238)
indices += range(257, 261)
indices += range(280, 286)
indices += range(303, 311)
indices += range(326, 334)
indices += range(347, 358)
indices += range(368, 380)
indices += range(387, 399)
indices += range(404, 442)

for base_filename in base_filenames:
    basefile_path = folder_path + base_filename
    for index in indices:
        print 'processing', basefile_path + file_index(index) + '_1D.csv'
        filename = basefile_path + file_index(index) + '_1D.csv'
        Qlist, IntAve = read_1D(filename)
        background_x, background_y = select_bckgrd(background_indices)
        save_results(background_x, background_y, Qlist, IntAve, index, base_filename)

        
        