"""
author: Fang Ren (SSRL)

9/21/2017
"""

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
    peak_width_max = []
    peak_width_min = []
    num_of_peaks = []
    for basefile_path in basefile_paths:
        while (index <= total_num_scan):
            print('processing', basefile_path + file_index(index) + '_bckgrd_subtracted_peak_analysis_GLS.csv')
            file_name = basefile_path + file_index(index) + '_bckgrd_subtracted_peak_analysis_GLS.csv'
            peak_info = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
            print(peak_info)
            try:
                peak_position.append(peak_info[2][0])
                peak_intensity.append(peak_info[2][1])
                peak_width_max.append(max(peak_info[2:, 2]))
                peak_width_min.append(min(peak_info[2:, 2]))
            except IndexError:
                peak_position.append(np.nan)
                peak_intensity.append(np.nan)
                peak_width_max.append(np.nan)
                peak_width_min.append(np.nan)
            num_of_peaks.append(peak_info.shape[0]-2)
            #print peak_info
            index += 1
        index = 1
    return peak_position, peak_intensity, peak_width_max, peak_width_min, num_of_peaks


## user input
folder_path = '..//..//..//data//CoTiZr//1D_spectra//peak_fitted_auto//'
base_filename1 = 'SampleB2_4_24x24_t30_'
basefile_path1 = folder_path + base_filename1

base_filename2 = 'SampleB2_5_24x24_t30_'
basefile_path2 = folder_path + base_filename2

base_filename3 = 'SampleB2_6_24x24_t30_'
basefile_path3 = folder_path + base_filename3

basefile_paths = [basefile_path3]
total_num_scan = 441

## Initialization
basefile_path1 = folder_path + base_filename1
index = 1;

peak_position, peak_intensity, peak_width_max, peak_width_min, num_of_peaks = read_data(total_num_scan, index, basefile_paths)

np.savetxt(folder_path + 'peak_info.csv', np.concatenate(([peak_position], [peak_width_max], [peak_width_min], [peak_intensity], [num_of_peaks])).T, header = 'peak_position, peak_width_max, peak_width_min, peak_intensity, num_of_peaks', delimiter = ',')
