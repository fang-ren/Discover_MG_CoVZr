# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:37:51 2016

@author: fangren, Travis Williams
"""


from peak_detection_matlab import peakdet
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
from os.path import basename
from scipy.optimize import curve_fit


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



path = '..//..//..//data//CoTiZr//1D_spectra//background_subtracted//'
save_path = '..//..//..//data//CoTiZr//1D_spectra//peak_fitted_auto//'


for filename in glob.glob(os.path.join(path, '*.csv')):
    if basename(filename)[-5] == 'd':
        print 'processing', filename
        data = np.genfromtxt(filename, delimiter = ',' )
        Qlist = data[:,0][:647]
        IntAve = data[:,1][:647]
        maxs, mins = peakdet(IntAve, 10)
        peaks = maxs[:,0].astype(int)
        peaks_accepted = []
        for peak in peaks:
            if Qlist[peak] < 2.1 or Qlist[peak] > 3.3:
                continue
            peaks_accepted.append(peak)
        guess = [2.0, 25, 0.233, 0.5, 3.5, 37, 0.15, 0.5]
        low = [1.95, 20, 0.1, 0, 3.45, 10, 0.1, 0]
        high = [2.1, 40, 0.3, 1, 3.55, 40, 0.4, 1]
        peaks = peaks_accepted
        print peak
        try:
            for peak in peaks:
                guess.append(Qlist[peak])
                low.append(Qlist[peak]-0.1)
                high.append(Qlist[peak]+0.1)

                guess.append(IntAve[peak])
                low.append(0)
                high.append(IntAve[peak]+10)

                guess.append(0.2)
                low.append(0)
                high.append(1)

                guess.append(0.5)
                low.append(0)
                high.append(1)
            popt, pcov = curve_fit(func, Qlist, IntAve, p0=guess, bounds = (low, high))
            #popt, pcov = curve_fit(func, Qlist, IntAve, p0=guess)
            fit = func(Qlist, *popt)
            plt.figure(1)
            plt.plot(Qlist, IntAve)
            plt.plot( Qlist, fit, 'r--')
            plt.plot(Qlist[peaks], IntAve[peaks], 'o')

            for i in range(0, len(popt), 4):
                ctr1 = popt[i]
                amp1 = popt[i+1]
                wid1 = popt[i+2]
                n1 = popt[i+3]
                curve1 = n1 * amp1 * np.exp( -4 * np.log(2) * ((Qlist - ctr1)/wid1)**2) + (1-n1) * amp1 * wid1**2 / 4 / ((Qlist-ctr1)**2 + wid1**2 / 4)
                plt.plot(Qlist, curve1)

            plt.savefig(save_path + basename(filename)[:-4] + '_peak_analysis_GLS')
            plt.close()

            popt = np.reshape(popt, (popt.size/4, 4))
            np.savetxt(save_path + basename(filename)[:-4] + '_peak_analysis_GLS.csv', popt, delimiter=",")
        except RuntimeError:
            print "Failed to fit", filename
            print "used the previous peak information"
            np.savetxt(save_path + basename(filename)[:-4] + '_peak_analysis_GLS.csv', popt, delimiter=",")
