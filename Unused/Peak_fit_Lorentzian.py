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
    for i in range(0, len(params), 3):
        ctr = params[i]
        amp = params[i+1]
        wid = params[i+2]
        y = y + amp * np.exp( -((x - ctr)/wid)**2)
    return y


path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\1Dfiles\\high_power_8_14_17\\background_subtracted_0921_14\\Good\\'
save_path = path + 'peak_fit_twoPeaks\\'
if not os.path.exists(save_path):
    os.makedirs(save_path)

for filename in glob.glob(os.path.join(path, '*.csv')):     
    if basename(filename)[-5] == 'd':
        print 'processing', filename
        data = np.genfromtxt(filename, delimiter = ',' )
        Qlist = data[:,0]
        IntAve = data[:,1]
        guess = []
        peak = [380,580] 
        guess.append(Qlist[peak[0]])
        guess.append(IntAve[peak[0]])
        guess.append(0.1)
        guess.append(Qlist[peak[1]])
        guess.append(IntAve[peak[0]])
        guess.append(0.1)
        try:
            popt, pcov = curve_fit(func, Qlist, IntAve, p0=guess)
            fit = func(Qlist, *popt)
            plt.figure(1)            
            plt.plot(Qlist, IntAve)
            plt.plot( Qlist, fit)
            ctr1 = popt[0]
            amp1 = popt[1]
            wid1 = popt[2]    
            ctr2 = popt[3]
            amp2 = popt[4]
            wid2 = popt[5]
            curve1 = amp1 * np.exp( -((Qlist - ctr1)/wid1)**2)
            curve2 = amp2 * np.exp( -((Qlist - ctr2)/wid2)**2)
            plt.plot(Qlist, curve1)
            plt.plot(Qlist, curve2)
            plt.show()
            plt.savefig(save_path + basename(filename)[:-4] + '_peak_analysis_Lorentzian')
            plt.close()
        
            popt = np.reshape(popt, (popt.size/3, 3))
            np.savetxt(save_path + basename(filename)[:-4] + '_peak_analysis_Lorentzian.csv', popt, delimiter=",")
            
        except RuntimeError:
            print "Failed to fit", filename
            print "used the previous peak information"
            np.savetxt(save_path + basename(filename)[:-4] + '_peak_analysis_Lorentzian.csv', popt, delimiter=",")
            
