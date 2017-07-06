"""
author: fangren
"""


import numpy as np
import imp
from plotTernary import plt_ternary_save

save_path = '..//..//figures//'

Zr_range = np.arange(0, 100, 1.5)
V_range = np.arange(0, 100, 1.5)

Co_list = []
V_list = []
Zr_list = []

label = []

def line(V1, Zr1, V2, Zr2):
    a = (Zr1-Zr2)/(V1-V2)
    b = (Zr1-a*V1)*100
    return a, b


top = line(0.4, 0, 0, 0.4)

meltspin_file = '..//..//data//meltspin_data.csv'
meltspin_data = np.genfromtxt(meltspin_file, delimiter=',')

measured = np.reshape(meltspin_data, (len(meltspin_data)/3, 3))

#print measured
measured_label = np.ones((len(meltspin_data)/3, 1))
print measured_label.shape, measured.shape
measured = np.concatenate((measured, measured_label), axis = 1)
print measured.shape

binary = [[93, 0, 7, 1], [92, 0, 8, 1], [91, 0, 9, 1], [90, 0, 10, 1], [89, 0, 11, 1], [88, 0, 12, 1], [22, 0, 78, 1], [30, 0, 70, 1],
          [36, 0, 64, 1], [53, 0, 47, 1]]

measured = np.concatenate((measured, binary))

for Zr in Zr_range:
    for V in V_range:
        Co = 100 - Zr - V
        if Co >=0 and Co <= 100:
            Zr_list.append(Zr)
            V_list.append(V)
            Co_list.append(Co)
            # print (V, Zr)
            if V>=3 and top[0] * V + top[1] <= Zr:
                label.append(0.3)
            else:
                label.append(0)


Co_list = np.array(Co_list)
V_list = np.array(V_list)
Zr_list = np.array(Zr_list)
label = np.array(label)

Co_list = Co_list[label != 0]
V_list = V_list[label != 0]
Zr_list = Zr_list[label != 0]
label = label[label != 0]


ternary_data = np.concatenate(([Co_list], [V_list], [Zr_list], [label]), axis=0).T

ternary_data = np.concatenate((ternary_data, measured))
plt_ternary_save(ternary_data, tertitle='', labelNames=('Co', 'V', 'Zr'), scale=100,
                             sv=True, svpth=save_path, svflnm= 'Figure2d.png',
                             cbl='Scale', vmax = 1, vmin = 0, cmap='gray_r', cb=True, style='h')