"""
author: Fang Ren (SSRL)

9/20/2017
"""

from shutil import copyfile
import os


def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)

source_folder = 'Sample5\\'
destination_folder = '1D_spectra\\raw_1D'
basename = 'Sample5_24x24_t30_'


index = 1
total_num_scan = 441
while (index <= total_num_scan):
    source = os.path.join(source_folder, basename + file_index(index) + '_1D.csv')
    print('copying', source)
    destination = os.path.join(destination_folder, basename + file_index(index) + '_1D.csv')
    copyfile(source, destination)
    index += 1