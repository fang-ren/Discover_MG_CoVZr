"""
Created on Feb 8, 2017

@author: fangren
"""

import os.path
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import basinhopping
from scipy.interpolate import interp1d
from numpy.polynomial.chebyshev import chebval



def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)


# set folder and save path
path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoVZr_ternary\\1Dfiles\\high_power_15'
save_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoVZr_ternary\\1Dfiles\\high_power_15\\backgrd_subtracted_1D'
basename = 'Sample15_7thick_24x24_t30_'

file_name_b = os.path.join(path, basename+'0233_1D.csv')

background = np.genfromtxt(file_name_b, delimiter=',')
intensity_b = background[:, 1][30:-100]
Q_b = background[:, 0][30:-100]

index = 1
total_num_scan = 441
while (index <= total_num_scan):
    file_name = os.path.join(path, basename + file_index(index) + '_1D.csv')
    print 'processing', file_name
    spectrum = np.genfromtxt(file_name, delimiter= ',')
    intensity = spectrum[:, 1][30:-100]
    Q =  spectrum[:, 0][30:-100]

    intensity_s = intensity - intensity_b*0.8
    intensity_s = np.subtract(intensity_s, intensity_s[0])
    # save the plot
    plt.figure(1)
    plt.subplot(211)
    plt.plot(Q, intensity)
    plt.plot(Q_b, intensity_b, 'o')
    plt.xlim(0.8, 5.8)
    plt.subplot(212)
    plt.plot(Q, intensity_s)
    plt.plot(Q, [0] * len(Q), 'r--')
    plt.xlim(0.8, 5.8)
    plt.savefig(os.path.join(save_path, basename + file_index(index) + '_bckgrd_subtracted.png'))
    plt.close('all')
    np.savetxt(os.path.join(save_path, basename + file_index(index) + '_bckgrd_subtracted.csv'), np.concatenate(([Q], [intensity_s])).T, delimiter= ',')
    index += 1