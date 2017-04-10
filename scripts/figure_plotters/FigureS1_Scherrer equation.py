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

lamda = 1.5406
K = 0.9  # shape factor

theta1 = np.array(range(1000))
theta1 = 0.00314 * theta1/4
theta2 = np.array(range(1000))
theta2 = 0.00314 * theta2/4

Q1 = 4 * np.pi * np.sin(theta1) / lamda
Q2 = 4 * np.pi * np.sin(theta2) / lamda


BETA = []
TAU = []
BETA_r = []

#theta = 0.61

for i in range(1000):
    for j in range(i, 1000):
        beta_in_Q = Q1[j] - Q2[i]
        beta_in_radian = (theta1[j] - theta2[i]) * 2
        theta = (theta1[j] + theta2[i])/2
        tau = K * lamda /(10* beta_in_radian * np.cos(theta))
        BETA.append(beta_in_Q)
        BETA_r.append(beta_in_radian)
        TAU.append(tau)


BETA_r = np.array(BETA_r)
BETA_degree = BETA_r * 180 / np.pi        

crystalline = [3.5] * len(BETA)
amorphous = [1] * len(BETA)


save_path = '..//..//figures//'

plt.figure(1)
plt.plot(TAU, BETA, label = 'Scherrer equation')
plt.plot(crystalline, BETA, label = 'crystalline, D > 3.5 nm')
plt.plot(amorphous, BETA, label = 'amorphous, D < 1.0 nm')
plt.ylabel('FWHM in Q')
plt.xlabel('D, nm')
plt.xscale('log')
plt.xlim((0.9, 100))
plt.ylim((0, 0.6))
plt.legend()
plt.savefig(save_path+'FigureS1.png', dpi = 600)
