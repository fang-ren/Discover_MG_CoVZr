# -*- coding: utf-8 -*-
"""
Created on 12/13 2016

@author: fangren
"""

import numpy as np
import matplotlib.pyplot as plt
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

silica_spectra_file = 'C:\Research_FangRen\Data\July2016\CoVZr_ternary\silica_xrd\\silica_XRD.csv'
silica_spectra = np.genfromtxt(silica_spectra_file, delimiter=',')

lamda = 1.54

twoTheta = silica_spectra[:, 0]
Q = 4*np.pi*np.sin(twoTheta/2/180*np.pi)/lamda
Intensity = silica_spectra[:, 1]-16.25

plt.plot(Q, Intensity, label = 'silica')

guess = [1.53, 70, 0.5, 0.5]
high = [1.63, 100, 1, 1, ]
low = [1.43, 20, 0.1, 0]

popt, pcov = curve_fit(func, Q, Intensity, p0=guess, bounds=(low, high))

fit = func(Q, *popt)
plt.plot(Q, fit, label = 'fit')
plt.xlabel('Q')
plt.ylabel('Intensity')
plt.legend()

print(popt)