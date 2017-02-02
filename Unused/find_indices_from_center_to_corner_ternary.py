# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:34:53 2016

@author: fangren
"""

"""
find indices
"""

import numpy as np

path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\masterfiles\\low\\'

filename = 'CLEANED_Sample9_24x24_t30_92236562master_metadata.csv'

data = np.genfromtxt(path+filename, delimiter=',', skip_header = 1)

Co = data[:,54]
V = data[:,55]
Zr = data[:,56]
scan_num = data[:,52]

scan_chosen = []
indices = []
for i in range(len(scan_num)):
    if np.abs(Zr[i] - V[i]) < 1:
        scan_chosen.append(scan_num[i])
        indices.append(i)

scan_chosen = map(int, scan_chosen)
print scan_chosen


print Co[indices]

