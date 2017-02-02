# -*- coding: utf-8 -*-
"""
PDF reconstruction

Created on Tue Aug 30 13:47:59 2016

@author: fangren
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(r, *params):
    """
    create a fitted curve according to params
    """
    Tr = np.zeros_like(r)
    for i in range(0, len(params), 4):
        w = params[i]
        rij = params[i+1]
        a = params[i+2]
        sigma = params[i+3]
        Tr = Tr + w*a/(np.sqrt(2*np.pi)*sigma) * np.exp( -((r - rij)**2/(2*sigma**2))) 
    return Tr
    
def Gaussian(r, *param):
    Tr = np.zeros_like(r)
    w = param[0]
    rij = param[1]
    a = param[2]
    sigma = param[3]
    Tr = Tr + w*a/(np.sqrt(2*np.pi)*sigma) * np.exp( -((r - rij)**2/(2*sigma**2)))
    return Tr

a = 1
sigma = 0.1
guess = [0.277, 2.59, a, sigma, 0.216, 2.85, a, sigma, 0.155, 2.94, a, sigma, 0.1, 2.04, a, sigma]

w = [0.277, 0.216, 0.193, 0.155, 0.1, 0.06, 0.1]

low = (0,2.54,0,0,0,2.8,0,0,0,2.89,0,0,0,2.03,0,0)
high = (100,2.64,100,0.2,100,2.9,100,0.2,100,2.99,100,0.2,100,2.05,100,0.2)

r = range(180, 360)
r = np.array(r)
r = r*0.01



path = 'C:\Research_FangRen\Publications\Combinatorial Search for Metallic Glasses in Co-V-Zr ternary systems\MG\\'

filename = 'PDF_r_G(r).csv'
fullname = path + filename



data = np.genfromtxt(fullname, delimiter=',', skip_header = 2)
#r = data[177:338,2]
#Gr = data[177:338,3]

r = data[177:338,0]
Gr = data[177:338,1]

#r = data[177:500,0]
#Gr = data[177:500,1]

Tr = Gr + 4*np.pi*0.066*r

#background = Gaussian(r, *[0.72, 3.4, 1.5, 0.35])
#background = Gaussian(r, *[0.85, 3.44, 1.5, 0.32])
#background = Gaussian(r, *[1.2, 3.44, 1.5, 0.32])
#background = Gaussian(r, *[0.62, 3.44, 1.5, 0.32])
background = Gaussian(r, *[1, 3.44, 1.5, 0.32])
Tr = Tr - background

plt.plot(r, Tr, 'o', label = 'unannealed PDF')
#plt.plot(r, background)
#plt.plot(r, Tr-background)


popt, pcov = curve_fit(func, r, Tr, p0=guess, bounds = (low, high))

# re-organizing parameters
popt[2] = popt[0]*popt[2]/w[0]
popt[0] = w[0]


popt[6] = popt[4]*popt[6]/w[1]
popt[4] = w[1]


popt[10] = popt[8]*popt[10]/w[2]
popt[8] = w[2]




fit = func(r, *popt)

Gaussian1 = Gaussian(r, *popt[:4])
Gaussian2 = Gaussian(r, *popt[4:8])
Gaussian3 = Gaussian(r, *popt[8:12])
Gaussian4 = Gaussian(r, *popt[12:16])

#
#plt.plot(r, Gaussian1, 'pink', label = 'Co-V')
#plt.plot(r, Gaussian2, 'y', label = 'Co-Zr')
#plt.plot(r, Gaussian3, 'g', label = 'Co-Co')
#plt.plot(r, Gaussian4, 'b', label = 'V-Zr')
#plt.plot(r, Gaussian5, 'purple', label = 'V-V')
#plt.plot(r, Gaussian6, 'orange', label = 'Zr-Zr')
#plt.plot(r, Gaussian7, '--r', label = 'Si-Si')

plt.plot(r, Gaussian1, 'pink')
plt.plot(r, Gaussian2, 'y')
plt.plot(r, Gaussian3, 'g')
plt.plot(r, Gaussian4, '--r')


plt.plot(r, fit, 'r', linewidth = 2.0, label = 'fit')

plt.plot(r, Tr-fit, 'black', linewidth = 2.0, label = 'intensity difference')

plt.xlim((1.8, 3.4))
plt.ylim((-0.5, 5))
plt.legend()
plt.xlabel('r')
plt.ylabel('T(r)')




def cn(c, a, rij, sigma):
    return c*a*(rij+sigma/np.sqrt(2*np.pi))    
    
i = 0
cn_Co_V = cn(0.38, popt[i+2], popt[i+1], popt[i+3])
cn_V_Co = cn(0.45, popt[i+2], popt[i+1], popt[i+3])
i = 4
cn_Co_Zr = cn(0.17, popt[i+2], popt[i+1], popt[i+3])
cn_Zr_Co = cn(0.45, popt[i+2], popt[i+1], popt[i+3])
i = 8
cn_V_Zr = cn(0.17, popt[i+2], popt[i+1], popt[i+3])
cn_Zr_V = cn(0.38, popt[i+2], popt[i+1], popt[i+3])


cn_Co_Co = 0
cn_V_V =  0
cn_Zr_Zr = 0


print cn_Co_V, cn_V_Co, cn_Co_Zr, cn_Zr_Co, cn_Co_Co, cn_V_Zr, cn_Zr_V, cn_V_V, cn_Zr_Zr

print popt[1],popt[5], popt[9], popt[13]

    