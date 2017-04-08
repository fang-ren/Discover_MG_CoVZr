"""
Created on Wed Aug 03 16:22:25 2016

@author: fangren
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep
import os



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
    print background_y[5]
    if background_y[5] >820:
        background_y[5] = 820
    
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
    plt.savefig(save_path + base_filename + file_index(index) + 'bckgrd_subtracted.png' )    
    
    plt.close('all')
    
    data = np.concatenate(([Qlist], [(IntAve-background)]), axis = 0)
    np.savetxt(save_path + base_filename + file_index(index) + 'bckgrd_subtracted.csv', data.T, delimiter=",")


# change the background indices according to each sample. Refering to background_selection.py to choosing the right background.
background_indices = [5,42, 92, 142, 180, 468, 548, 584, 841, 863, 882, 895, 903, 925]


sample_num = 'Sample8'
base_filename = 'Sample8_24x24_t30_'

folder_path = '..//..//..//data//1D_spectra//raw_1D//' + sample_num + '//'
save_path = '..//..//..//data//1D_spectra//background_subtracted//' + sample_num + '//'
if not os.path.exists(save_path):
    os.makedirs(save_path)

index = 1
basefile_path = folder_path + base_filename
while (index <= 440):
    print 'processing', basefile_path + file_index(index) + '_1D.csv'
    filename = basefile_path + file_index(index) + '_1D.csv'
    Qlist, IntAve = read_1D(filename)
    background_x, background_y = select_bckgrd(background_indices)
    save_results(background_x, background_y, Qlist, IntAve, index, base_filename)
    index += 1
        
        