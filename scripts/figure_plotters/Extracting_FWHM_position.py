"""
author: Fang Ren (SSRL)

3/23/2017
"""


import numpy as np
import imp
plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")

path = '..//..//data//master_data//'
save_path = '..//..//figures//'

basename1 = 'CLEANED_Sample9_master_metadata_low.csv'
basename2 = 'CLEANED_Sample10_master_metadata_low.csv'
basename3 = 'CLEANED_Sample18_master_metadata_low.csv'


filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)
data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)
data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)

data = np.concatenate((data1[:, :69], data2[:, :69], data3[:, :69]))

Co = data[:,57]*100
V = data[:,58]*100
Zr = data[:,59]*100
peak_position = data[:,60]
peak_width = data[:,61]
peak_intensity = data[:,62]
peak_width_neighborhood = np.copy(peak_width)



"""
V = 0.1, Zr = 0.0; V = 0.3, Zr = 0.7
"""

def line(V1, Zr1, V2, Zr2):
    a = (Zr1-Zr2)/(V1-V2)
    b = (Zr1-a*V1)*100
    return a, b

selected = line(0.1, 0.0, 0.3, 0.7)


FWHM = []
position = []
indices = []
Co_list = []
V_list = []
Zr_list = []

for i in range(len(Co)):
    if abs(selected[0]*V[i] + selected[1] - Zr[i]) < 1:
        Zr_list.append(Zr[i])
        V_list.append(V[i])
        Co_list.append(Co[i])
        FWHM.append(peak_width[i])
        position.append(peak_position[i])


np.savetxt(save_path+'extracted_values.csv', np.concatenate(([Co_list], [V_list], [Zr_list], [FWHM], [position])).T, delimiter= ',', header = 'Co, V, Zr, FWHM, peak_position')


ternary_data = np.concatenate(([Co_list],[V_list],[Zr_list],[FWHM]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='extracted',
                       cbl='FWHM', cmap='viridis_r', cb=True, style='h')
