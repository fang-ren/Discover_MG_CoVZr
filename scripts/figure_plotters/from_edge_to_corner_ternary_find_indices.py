# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:34:53 2016

@author: fangren
"""

"""
find indices
"""

import numpy as np
#
# # high power
# path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\masterfiles\\high\\'
# save_path = path + 'plots\\'
#
# basename1 = 'CLEANED_Sample8_master_metadata_high_WDS_Travis.csv'
# basename2 = 'CLEANED_Sample14_master_metadata_high.csv'
# basename3 = 'CLEANED_Sample17_master_metadata_high_WDS.csv'
#
# filename1 = path + basename1
# filename2 = path + basename2
# filename3 = path + basename3
#
# data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)[:, :69]
# data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)[:, :69]
# data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)[:, :69]
#
# data = data1


# low power

path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\masterfiles\\low\\'
save_path = path + 'plots\\'

basename1 = 'CLEANED_Sample9_master_metadata_low.csv'
basename2 = 'CLEANED_Sample10_master_metadata_low.csv'
basename3 = 'CLEANED_Sample18_master_metadata_low.csv'

filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)[:, :69]
data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)[:, :69]
data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)[:, :69]

data = data2


Co = data[:,57]*100
V = data[:,58]*100
Zr = data[:,59]*100
scan_num = data[:,52]

scan_chosen = []
indices = []
for i in range(len(scan_num)):
    if np.abs(Co[i] - V[i]) < 1:
        scan_chosen.append(scan_num[i])
        indices.append(i)

scan_chosen = list(map(int, scan_chosen))
print(scan_chosen)


print(Zr[indices])

