"""
author: Fang Ren (SSRL)

3/22/2017
"""

import numpy as np

## user input
folder_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\FeNbTi\\XRF\\MCA_files\\XRF_channels_fit_21\\'
base_filename = 'SampleB2_21_24x24_t30_'

save_path = folder_path

## Initialization
basefile_path = folder_path + base_filename
index = 1
total_num_scan = 440


Ti_alpha = []
Ti_beta = []
Fe_alpha = []
Fe_beta = []

while (index <= total_num_scan):
    print 'processing', basefile_path + str(index) + '_XRF_fit.csv'
    file_name = basefile_path + str(index) + '_XRF_fit.csv'
    XRF_info = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
    Ti_alpha.append(XRF_info[0][0])
    Ti_beta.append(XRF_info[0][1])
    Fe_alpha.append(XRF_info[0][2])
    Fe_beta.append(XRF_info[0][3])
    index += 1

XRF_channels = np.concatenate(([Ti_alpha], [Ti_beta], [Fe_alpha], [Fe_beta]), axis = 0)
print XRF_channels.T.shape


header_string = 'Ti_alpha,Ti_beta,Fe_alpha,Fe_beta'
# print header_string
np.savetxt(save_path + base_filename + 'XRF.csv', XRF_channels.T, delimiter=",", header= header_string)