# -*- coding: utf-8 -*-
"""
Created on Mon Aug 08 11:09:47 2016

@author: fangren
"""

import matplotlib.pyplot as plt
from scipy.interpolate import splev, splrep
import numpy as np

# try changing the background_indices to choose the best point for spline fit
background_indices = [5,42, 92, 142, 180, 514, 925] 

path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\1Dfiles\\high_power_15\\'
filename = 'Sample15_7thick_24x24_t30_0056_1D.csv'

fullname = path + filename

def read_1D(filename):
    data = np.genfromtxt(filename, delimiter=',', skip_header = 0)
    Qlist = data[:,0][8:937]
    IntAve = data[:,1][3:][8:937]
    return Qlist, IntAve

Qlist, IntAve = read_1D(fullname)

x = range(0,929)

background_x = Qlist[background_indices]
background_y = IntAve[background_indices]


tck = splrep(background_x,background_y)
    
background = splev(Qlist, tck)

plt.plot(x, IntAve)
plt.plot(background_indices, background_y, 'o')
plt.plot(x, background)

