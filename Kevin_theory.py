"""
author: Fang Ren (SSRL)

3/23/2017
"""


import numpy as np
import imp

plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")

save_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoVZr_ternary\\Theory\\'

Zr_range = np.arange(0, 100, 1.5)
V_range = np.arange(0, 100, 1.5)

Co = []
V = []
Zr = []

label = []

"""
Upper: Zr = 0.49, V = 0; Zr = 0.32, V = 0.68
lower: Zr = 0.32, V = 0; Zr = 0.15, V = 0.85
"""


for i in Zr_range:
    for j in V_range:
        if i + j <= 100 and i + j >= 0:
            try:
                Zr.append(i)
                V.append(j)
                Co.append(100 - i - j)
                if i+ 0.25*j <= 49 and i + 0.2*j >= 32:
                    label.append(1)
                elif i+ 0.25*j <= 59 and i + 0.2*j >= 22:
                    label.append(0.5)
                else:
                    label.append(0)
            except(ValueError):
                continue

ternary_data = np.concatenate(([Co], [V], [Zr], [label]), axis=0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('Co', 'V', 'Zr'), scale=100,
                             sv=True, svpth=save_path, svflnm= 'Kevin_prediction.png',
                             cbl='Scale', vmax = 1.4, vmin = -0.1, cmap='viridis_r', cb=True, style='h')