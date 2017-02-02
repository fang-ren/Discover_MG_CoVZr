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
        y = y + n * amp * np.exp( -((x - ctr)/wid)**2) + (1-n) * amp * wid**2 / ((x-ctr)**2 + wid**2)
    return y


path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\1Dfiles\\low_power_9_10_18\\Sample9\\background_subtracted\\'
base_file = 'Sample9_24x24_t30_0434bckgrd_subtracted.csv'
filename = path + base_file
save_path = path + 'peak_fit_threePeaks_Voigt\\'
if not os.path.exists(save_path):
    os.makedirs(save_path)


guess = [2.1, 36.4, 0.233, 0.5, 3.1, 5000, 0.33, 0.5, 3.4, 17.7, 0.15, 0.5]
high = [2.15, 50, 0.3, 1, 3.4, 10000, 0.8, 1, 3.5, 40, 0.2, 1]
low = [2.05, 0, 0.1, 0, 2.1, 0, 0, 0, 3.3, 0, 0.1, 0]


data = np.genfromtxt(filename, delimiter = ',' )
Qlist = data[:,0][:594]
IntAve = data[:,1][:594]

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
ctr3 = popt[8]
amp3 = popt[9]
wid3 = popt[10]  
n3 = popt[11]
curve1 = n1 * amp1 * np.exp( -((Qlist - ctr1)/wid1)**2) + (1-n1) * amp1 * wid1**2 / ((Qlist-ctr1)**2 + wid1**2)
curve2 = n2 * amp2 * np.exp( -((Qlist - ctr2)/wid2)**2) + (1-n2) * amp2 * wid2**2 / ((Qlist-ctr2)**2 + wid2**2)
curve3 = n3* amp3 * np.exp( -((Qlist - ctr3)/wid3)**2) + (1-n3) * amp3 * wid3**2 / ((Qlist-ctr3)**2 + wid3**2)
plt.plot(Qlist, curve1)
plt.plot(Qlist, curve2)
plt.plot(Qlist, curve3)
plt.show()
plt.savefig(save_path + basename(filename)[:-4] + '_peak_analysis_Voigt')
plt.close()

popt = np.reshape(popt, (popt.size/4, 4))
np.savetxt(save_path + basename(filename)[:-4] + '_peak_analysis_Voigt.csv', popt, delimiter=",")


