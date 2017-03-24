"""
author: Fang Ren (SSRL)

3/23/2017
"""


import numpy as np
import imp

plotTernary = imp.load_source("plt_ternary_save", "plotTernary_Kevin.py")

save_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoVZr_ternary\\Theory\\'

Zr_range = np.arange(0, 100, 1.05)
V_range = np.arange(0, 100, 1.05)

Co_list = []
V_list = []
Zr_list = []

label = []

"""
2% : V = 0.071, Zr = 0.526; V = 0.504, Zr = 0.413
-2%: V = 0.071, Zr = 0.363; V = 0.697, Zr = 0.22

1%: V = 0.071, Zr = 0.476; V = 0.557, Zr = 0.36
-1%: V = 0.071, Zr = 0.419; V = 0.638, Zr = 0.279

Zr corner: V = 0, Zr = 0.82; V = 0.19, Zr = 0.81
Co corner: V = 0, Zr = 0.18; V = 0.34, Zr = 0
V corner: V = 0.65, Zr = 0; V = 0.6, Zr = 0.4
"""

def line(V1, Zr1, V2, Zr2):
    a = (Zr1-Zr2)/(V1-V2)
    b = (Zr1-a*V1)*100
    return a, b

plus2 = line(0.071, 0.526, 0.504, 0.413)
negative2 = line(0.071, 0.363, 0.697, 0.22)

plus1 = line(0.071, 0.476, 0.557, 0.36)
negative1 = line(0.071, 0.419, 0.638, 0.279)

Zr_corner = line(0, 0.82, 0.19, 0.81)
Co_corner = line(0, 0.18, 0.34, 0)
V_corner = line(0.65, 0, 0.6, 0.4)

for Zr in Zr_range:
    for V in V_range:
        Co = 100 - Zr - V
        if Co >=0 and Co <= 100:
            Zr_list.append(Zr)
            V_list.append(V)
            Co_list.append(Co)
            if Zr >= Zr_corner[0]*V + Zr_corner[1] or Zr >= V_corner[0]*V + V_corner[1] or Zr < Co_corner[0]*V + Co_corner[1]:
                label.append(5)
            else:
                if V > 7.1 and Co >= 8.3:
                    if plus1[0]*V + plus1[1] >= Zr and negative1[0]*V + negative1[1] <= Zr:
                        label.append(1)
                    elif plus2[0]*V + plus2[1] >= Zr and negative2[0]*V + negative2[1] <= Zr:
                        label.append(0.5)
                    else:
                        label.append(0)
                else:
                    label.append(0)



ternary_data = np.concatenate(([Co_list], [V_list], [Zr_list], [label]), axis=0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('Co', 'V', 'Zr'), scale=100,
                             sv=True, svpth=save_path, svflnm= 'Kevin_prediction.png',
                             cbl='Scale', vmax = 1.4, vmin = -0.1, cmap='viridis_r', cb=True, style='h')