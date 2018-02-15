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


def func(x, *params):
    """
    create a Gaussian fitted curve according to params
    """
    y = np.zeros_like(x)
    # Ti alpha
    ctr1 = params[0]
    amp1 = params[1]
    wid1 = params[2]
    # Ti beta, refer to the paper (Smith_et_al-1974-X-Ray_Spectrometry) for the value of beta/alpha ratio
    ctr2 = params[3]
    amp2 = params[1]*0.131
    wid2 = params[4]
    # Fe alpha
    ctr3 = params[5]
    amp3 = params[6]
    wid3 = params[7]
    # Fe beta, refer to the paper (Smith_et_al-1974-X-Ray_Spectrometry) for the value of beta/alpha ratio
    ctr4 = params[8]
    amp4 = params[6]*0.136
    wid4 = params[9]
    # impurity Mn alpha
    ctr5 = params[10]
    amp5 = params[11]
    wid5 = params[12]
    # impurity Mn beta
    ctr6 = params[13]
    amp6 = params[11]*0.135
    wid6 = params[14]
    # impurity Sc alpha
    ctr7 = params[15]
    amp7 = params[16]
    wid7 = params[17]
    # impurity Sc beta
    ctr8 = params[18]
    amp8 = params[16]*0.13
    wid8 = params[19]
    # impurity Co alpha
    ctr9 = params[20]
    amp9 = params[21]
    wid9 = params[22]
    # impurity Co beta
    ctr10 = params[23]
    amp10 = params[21]*0.137
    wid10 = params[24]
    y = y + \
        amp1 * np.exp( -((x - ctr1)/wid1)**2) + \
        amp2 * np.exp( -((x - ctr2)/wid2)**2) + \
        amp3 * np.exp( -((x - ctr3)/wid3)**2) + \
        amp4 * np.exp( -((x - ctr4)/wid4)**2) + \
        amp5 * np.exp(-((x - ctr5) / wid5) ** 2) + \
        amp6 * np.exp(-((x - ctr6) / wid6) ** 2) + \
        amp7 * np.exp(-((x - ctr7) / wid7) ** 2) + \
        amp8 * np.exp(-((x - ctr8) / wid8) ** 2) + \
        amp9 * np.exp(-((x - ctr9) / wid9) ** 2) + \
        amp10 * np.exp(-((x - ctr10) / wid10) ** 2)
    return y



# path
path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\FeNbTi\\XRF\\MCA_files\\'
base_filename = 'SampleB2_21_24x24_t30_scan1_mca.dat'

filename = path + base_filename
save_path = path + 'XRF_channels_fit\\'
if not os.path.exists(save_path):
    os.makedirs(save_path)

data = np.genfromtxt(filename, delimiter=' ')
x = np.array(list(range(data.shape[1])))


# # visualize a few XRF spectra for defining peak positions.
# y1 = data[1, :]
# y2 = data[100, :]
# y3 = data[300, :]
# y4 = data[440, :]
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)
# plt.plot(x, y4)


# initialize guesses and high and low bounds for fitting, refer to the excel file for peak calibration
guess = [480, 1000, 10,
         525, 10,
         681, 1000, 10,
         751, 10,
         628, 1000, 10,
         692, 10,
         435, 1000, 10,
         475, 10,
         736, 1000, 10,
         814, 10]
high = [500, 50000, 30,
        545, 30,
        701, 50000, 30,
        771, 30,
        648, 50000, 30,
        712, 30,
        455, 50000, 30,
        495, 30,
        756, 50000, 30,
        834, 30]
low = [460, 0, 0,
       505, 0,
       661, 0, 0,
       731, 0,
       608, 0, 0,
       672, 0,
       415, 0, 0,
       455, 0,
       716, 0, 0,
       794, 0]

# fitting starts from here
for i in range(1, data.shape[0]):
    print(i)
    intensity = data[i]
    try:
        popt, pcov = curve_fit(func, x, intensity, p0=guess, bounds = (low, high))
        fit = func(x, *popt)
        plt.figure(1)
        plt.plot(x, intensity)
        plt.plot(x, fit)
        ctr1 = popt[0]
        amp1 = popt[1]
        wid1 = popt[2]

        ctr2 = popt[3]
        amp2 = popt[1] * 0.131
        wid2 = popt[4]

        ctr3 = popt[5]
        amp3 = popt[6]
        wid3 = popt[7]

        ctr4 = popt[8]
        amp4 = popt[6] * 0.136
        wid4 = popt[9]

        ctr5 = popt[10]
        amp5 = popt[11]
        wid5 = popt[12]

        ctr6 = popt[18]
        amp6 = popt[16] * 0.135
        wid6 = popt[19]

        ctr7 = popt[15]
        amp7 = popt[16]
        wid7 = popt[17]

        ctr8 = popt[18]
        amp8 = popt[16] * 0.13
        wid8 = popt[19]

        ctr9 = popt[20]
        amp9 = popt[21]
        wid9 = popt[22]

        ctr10 = popt[23]
        amp10 = popt[21] * 0.137
        wid10 = popt[24]

        curve1 = amp1 * np.exp( -((x - ctr1)/wid1)**2)
        curve2 = amp2 * np.exp( -((x - ctr2)/wid2)**2)
        curve3 = amp3 * np.exp( -((x - ctr3)/wid3)**2)
        curve4 = amp4 * np.exp( -((x - ctr4)/wid4)**2)
        curve5 = amp5 * np.exp(-((x - ctr5) / wid5) ** 2)
        curve6 = amp6 * np.exp(-((x - ctr6) / wid6) ** 2)
        curve7 = amp7 * np.exp(-((x - ctr7) / wid7) ** 2)
        curve8 = amp8 * np.exp(-((x - ctr8) / wid8) ** 2)
        curve9 = amp9 * np.exp(-((x - ctr9) / wid9) ** 2)
        curve10 = amp10 * np.exp(-((x - ctr10) / wid10) ** 2)

        plt.plot(x, curve1)
        plt.plot(x, curve2)
        plt.plot(x, curve4)
        plt.plot(x, curve3)
        plt.plot(x, curve5)
        plt.plot(x, curve6)
        plt.plot(x, curve7)
        plt.plot(x, curve8)
        plt.plot(x, curve9)
        plt.plot(x, curve10)

        plt.xlim(380, 1000)
        print('saving', save_path + base_filename[:-13] + str(i) + '_XRF_fit')
        plt.savefig(save_path + base_filename[:-13] + str(i) + '_XRF_fit')
        plt.close()
        result = [[amp1, amp2, amp3, amp4, amp5, amp6, amp7, amp8, amp9, amp10], [ctr1, ctr2, ctr3, ctr4, ctr5, ctr6, ctr7, ctr8, ctr9, ctr10], [wid1, wid2, wid3, wid4, wid5, wid6, wid7, wid8, wid9, wid10]]
        np.savetxt(save_path + base_filename[:-13] + str(i) + '_XRF_fit.csv', result, delimiter=",")
    except RuntimeError:
        print("Failed to fit", i+1)
        print("used the previous peak information")
        np.savetxt(save_path + base_filename[:-13] + str(i) + '_XRF_fit.csv', result, delimiter=",")

