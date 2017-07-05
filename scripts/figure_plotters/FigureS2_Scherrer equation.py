# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 09:37:57 2016

@author: fangren
"""

"""
Scherrer equation
"""

import numpy as np
import matplotlib.pyplot as plt

lamda = 0.9762 # x-ray energy
K = 0.9  # shape factor

# set up theta1 and theta2, both of them range from 0 to np.pi/4, the units are radian
theta1 = np.array(range(1000))
theta1 = 0.00314 * theta1/4
theta2 = np.array(range(1000))
theta2 = 0.00314 * theta2/4

Q1 = 4 * np.pi * np.sin(theta1) / lamda
Q2 = 4 * np.pi * np.sin(theta2) / lamda


BETA_Q = []
TAU = []
BETA_radian = []

#theta = 0.61

for i in range(1000):
    for j in range(i, 1000):
        beta_in_Q = Q1[j] - Q2[i]
        beta_in_radian = (theta1[j] - theta2[i]) * 2
        theta = (theta1[j] + theta2[i])/2
        tau = K * lamda /(10* beta_in_radian * np.cos(theta))  # the factor 10 changes the unit from angstrom to nm
        BETA_Q.append(beta_in_Q)
        BETA_radian.append(beta_in_radian)
        TAU.append(tau)


BETA_radian = np.array(BETA_radian)
BETA_degree = BETA_radian * 180 / np.pi

crystalline = [3.5] * len(BETA_Q)
amorphous = [1] * len(BETA_Q)


save_path = '..//..//figures//'

plt.figure(1)
plt.plot(TAU, BETA_Q, label = 'Scherrer equation')
plt.plot(crystalline, BETA_Q, label = 'crystalline, D > 3.5 nm')
plt.plot(amorphous, BETA_Q, label = 'amorphous, D < 1.0 nm')
plt.ylabel('FWHM in Q')
plt.xlabel('D, nm')
plt.xscale('log')
plt.xlim((0.9, 100))
plt.ylim((0, 0.6))
plt.legend()
plt.savefig(save_path+'FigureS2.png', dpi = 600)


# to plot the scherrer equation using Bragg angles (degrees), uncomment the following code
plt.figure(2)
plt.plot(TAU, BETA_degree)
plt.xlim(0, 6)