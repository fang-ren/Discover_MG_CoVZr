# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:37:51 2016

@author: fangren
"""

import matplotlib.pyplot as plt
import numpy as np
import glob
import os
from os.path import basename
from scipy.optimize import curve_fit
import imp
import os.path

peakdet = imp.load_source("peakdet", "peak_detection.py")
    

def func(x, *params):
    """
    create a Lorentzian fitted curve according to params
    """
    y = np.zeros_like(x)
    for i in range(0, len(params), 4):
        ctr = params[i]
        amp = params[i+1]
        wid = params[i+2]
        n = params[i+3]
        y = y + n * amp * np.exp(-4 * np.log(2) * ((x - ctr) / wid) ** 2) + (1 - n) * amp * wid ** 2 / 4 / (
        (x - ctr) ** 2 + wid ** 2 / 4)
    return y

def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)

path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\FeNbTi\\ID\\backgrd_subtracted_1D\\'
save_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\FeNbTi\\ID\\Peak_fitting_GLS\\'
base_name = 'SampleB2_21_24x24_t30_'

# parameters for 21
guess = [ 2.8, 5000, 0.33, 0.5, 3.4, 23, 0.15, 0.5]
high = [3.4, 10000, 1, 1, 3.5, 30, 0.2, 1]
low = [2.1, 0, 0, 0, 3.3, 10, 0.1, 0]

# # parameters for 19, 20
# guess = [3.9, 100, 0.3, 0.5, 2.8, 5000, 0.33, 0.5]
# high = [4.0, 175, 0.5, 1, 3.4, 10000, 1, 1]
# low = [3.8, 75, 0.1, 0, 2.1, 0, 0, 0]


for index in np.arange(1, 442):
    filename = os.path.join(path, base_name + file_index(index) + '_bckgrd_subtracted.csv')
    print 'processing', filename
    data = np.genfromtxt(filename, delimiter = ',' )
    Qlist = data[:,0][:647]
    IntAve = data[:,1][:647]
    try:
        data = np.genfromtxt(filename, delimiter = ',' )
        Qlist = data[:,0][:647]
        IntAve = data[:,1][:647]

        popt, pcov = curve_fit(func, Qlist, IntAve, p0=guess, bounds = (low, high))
        fit = func(Qlist, *popt)
        plt.figure(1)
        plt.plot(Qlist, IntAve)
        plt.plot( Qlist, fit)
        ctr1 = popt[0]
        amp1 = popt[1]
        wid1 = popt[2]
        n1 = popt[3]
        ctr2 = popt[4]
        amp2 = popt[5]
        wid2 = popt[6]
        n2 = popt[7]
        # ctr3 = popt[8]
        # amp3 = popt[9]
        # wid3 = popt[10]
        # n3 = popt[11]
        curve1 = n1 * amp1 * np.exp( -4 * np.log(2) * ((Qlist - ctr1)/wid1)**2) + (1-n1) * amp1 * wid1**2 / 4 / ((Qlist-ctr1)**2 + wid1**2 / 4)
        curve2 = n2 * amp2 * np.exp( -4 * np.log(2) * ((Qlist - ctr2)/wid2)**2) + (1-n2) * amp2 * wid2**2 / 4 / ((Qlist-ctr2)**2 + wid2**2 / 4)
        #curve3 = n3 * amp3 * np.exp( -4 * np.log(2) * ((Qlist - ctr3)/wid3)**2) + (1-n3) * amp3 * wid3**2 / 4 / ((Qlist-ctr3)**2 + wid3**2 / 4)
        plt.plot(Qlist, curve1)
        plt.plot(Qlist, curve2)
        #plt.plot(Qlist, curve3)
        plt.savefig(save_path + basename(filename)[:-4] + '_peak_analysis_GLS')
        plt.close()

        popt = np.reshape(popt, (popt.size/4, 4))
        np.savetxt(save_path + basename(filename)[:-4] + '_peak_analysis_GLS.csv', popt, delimiter=",")

    except RuntimeError:
        print "Failed to fit", filename
        print "used the previous peak information"
        np.savetxt(save_path + basename(filename)[:-4] + '_peak_analysis_GLS.csv', popt, delimiter=",")
            
    index += 1