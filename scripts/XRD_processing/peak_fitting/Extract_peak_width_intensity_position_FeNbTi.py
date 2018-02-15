# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 16:22:25 2016

@author: fangren
"""

import numpy as np

def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)

def read_data(total_num_scan, index, basefile_paths):
    peak_position = []
    peak_intensity = []
    peak_width = []
    while (index <= total_num_scan):
        print('processing', basefile_path + file_index(index) + '_bckgrd_subtracted_peak_analysis_GLS.csv')
        file_name = basefile_path + file_index(index) + '_bckgrd_subtracted_peak_analysis_GLS.csv'
        peak_info = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
        peak_position.append(peak_info[1][0])
        peak_intensity.append(peak_info[1][1])
        peak_width.append(peak_info[1][2])
        index += 1
    return peak_position, peak_intensity, peak_width


# ## user input high power
# folder_path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\1Dfiles\\high_power_8_14_17\\'
# base_filename1 = 'sample8\\background_subtracted\\peak_fit_Voigt\\Sample8_24x24_t30_'
# base_filename2 = 'sample14\\background_subtracted\\peak_fit_Voigt\\Sample14_7thin_24x24_t30_'
# base_filename3 = 'sample17\\background_subtracted\\peak_fit_Voigt\\Sample17_24x24_t30_'
# total_num_scan = 441


# user input low power
folder_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\FeNbTi\\ID\\Peak_fitting_GLS\\SampleB2_20\\'
base_filename = 'SampleB2_20_24x24_t30_'
total_num_scan = 441

## Initialization
basefile_path = folder_path + base_filename
index = 1;


peak_position, peak_intensity, peak_width = read_data(total_num_scan, index, basefile_path)

peak_info = np.concatenate(([peak_position], [peak_width], [peak_intensity])).T
np.savetxt(folder_path + 'peak_info.csv', peak_info,  header = 'peak_position, peak_width, peak_intensity', delimiter = ',')

