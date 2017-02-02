# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:27:27 2016

@author: fangren
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec



path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\Overlapping_region\\'

filename1 = 'Sample8_24x24_t30_0234bckgrd_subtracted.csv'
filename2 = 'Sample8_24x24_t30_0235bckgrd_subtracted.csv'
filename3 = 'Sample8_24x24_t30_0236bckgrd_subtracted.csv'
filename4 = 'Sample17_24x24_t30_0323bckgrd_subtracted.csv'
filename5 = 'Sample17_24x24_t30_0324bckgrd_subtracted.csv'
filename6 = 'Sample17_24x24_t30_0325bckgrd_subtracted.csv'

factor = 1
difference = 0

fullname = path + filename1
spectrum = np.genfromtxt(fullname, delimiter=',', skip_header = 0)
IntAve = spectrum[:,1]
Qlist = spectrum[:,0]
plt.plot(Qlist, IntAve, label = 'sample 8, 234')

fullname = path + filename2
spectrum = np.genfromtxt(fullname, delimiter=',', skip_header = 0)
IntAve = spectrum[:,1]
Qlist = spectrum[:,0]
plt.plot(Qlist, IntAve, label = 'sample 8, 235')

fullname = path + filename3
spectrum = np.genfromtxt(fullname, delimiter=',', skip_header = 0)
IntAve = spectrum[:,1]
Qlist = spectrum[:,0]
plt.plot(Qlist, IntAve, label = 'sample 8, 236')

fullname = path + filename4
spectrum = np.genfromtxt(fullname, delimiter=',', skip_header = 0)
IntAve = spectrum[:,1] * factor + difference
Qlist = spectrum[:,0]
plt.plot(Qlist, IntAve, label = 'sample 17, 323')

fullname = path + filename5
spectrum = np.genfromtxt(fullname, delimiter=',', skip_header = 0)
IntAve = spectrum[:,1] * factor + difference
Qlist = spectrum[:,0]
plt.plot(Qlist, IntAve, label = 'sample 17, 324')

fullname = path + filename6
spectrum = np.genfromtxt(fullname, delimiter=',', skip_header = 0)
IntAve = spectrum[:,1] * factor + difference
Qlist = spectrum[:,0]
plt.plot(Qlist, IntAve, label = 'sample 17, 325')

plt.xlim((1.5, 4))
# plt.ylim((600, 1100))
plt.ylabel('Intensity')
plt.xlabel('Q')
plt.legend()
plt.grid()
