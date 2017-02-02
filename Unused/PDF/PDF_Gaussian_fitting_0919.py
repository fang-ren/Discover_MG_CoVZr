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
    create a fitted curve  according to eq(2) in Ma's paper
    """
    Tr = np.zeros_like(r)
    for i in range(0, len(params), 3):
        weight = w[i/3]
        rij = params[i]
        a = params[i+1]
        sigma = params[i+2]
        Tr = Tr + weight*a/(np.sqrt(2*np.pi)*sigma) * np.exp( -((r - rij)**2/(2*sigma**2))) 
    return Tr
    
    
def Gaussian(r, *param):
    """
    for plotting Gaussian curve for each M-M pair. param is an array of lenth 4
    """
    Tr = np.zeros_like(r)
    w = param[0]
    rij = param[1]
    a = param[2]
    sigma = param[3]
    Tr = Tr + w*a/(np.sqrt(2*np.pi)*sigma) * np.exp( -((r - rij)**2/(2*sigma**2)))
    return Tr


# initialization 
w = [0.277, 0.216, 0.193, 0.155, 0.1, 0.06, 0.1]
guess = [2.59,1,0.1,2.85,1,0.1,2.50,0,0.1,2.94,1,0.1,2.68,0,0.1,3.4,0,0.1,2.03,1,0.1]

# setting constraint
low = (2.54,0,0,2.8,0,0,2.45,0,0,2.89,0,0,2.63,0,0,3.15,0,0,2.01,0,0)
high = (2.64,100,0.2,2.9,100,0.2,2.55,100,0.2,2.99,100,0.2,2.73,100,0.2,3.5,100,0.2,2.05,100,0.2)

## setting constraint (less strict)
#low = (2.5,0,0,2.75,0,0,2.4,0,0,2.84,0,0,2.58,0,0,3.1,0,0,2.01,0,0)
#high = (2.69,100,0.2,2.95,100,0.2,2.6,2,0.2,3.04,100,0.2,2.78,100,0.2,3.3,1,0.2,2.05,100,0.2)



path = 'C:\Research_FangRen\Publications\Combinatorial Search for Metallic Glasses in Co-V-Zr ternary systems\MG\\'

filename = 'PDF_r_G(r).csv'
fullname = path + filename


####################
### Unannealed sample
####################
#
#data = np.genfromtxt(fullname, delimiter=',', skip_header = 2)
#r = data[177:360,0]
#Gr = data[177:360,1]
#gr = Gr + 1
##rho_0 = 0.068
#rho_0 = 0.05
#rho_r = gr*rho_0
#Tr = 4*np.pi*r *rho_r
#
#plt.plot(r, Tr, 'o', label = 'unannealed PDF')
#
##initial_guess = func(r, *guess)
##plt.plot(r, initial_guess)

#
###################
## annealed sample
###################

data = np.genfromtxt(fullname, delimiter=',', skip_header = 2)
r = data[177:360,2]
Gr = data[177:360,3]

gr = Gr + 1
#rho_0 = 0.068
rho_0 = 0.05
rho_r = gr*rho_0
Tr = 4*np.pi*r *rho_0 + Gr * 4*np.pi*r *rho_0

plt.plot(r, Tr, 'o', label = 'unannealed PDF')

#initial_guess = func(r, *guess)
#plt.plot(r, initial_guess)

##################
# start fitting
##################

popt, pcov = curve_fit(func, r, Tr, p0=guess, bounds = (low, high))
fit = func(r, *popt)

Gaussian1 = Gaussian(r, *np.concatenate([[w[0]],popt[:3]]))
Gaussian2 = Gaussian(r, *np.concatenate([[w[1]],popt[3:6]]))
Gaussian3 = Gaussian(r, *np.concatenate([[w[2]],popt[6:9]]))
Gaussian4 = Gaussian(r, *np.concatenate([[w[3]],popt[9:12]]))
Gaussian5 = Gaussian(r, *np.concatenate([[w[4]],popt[12:15]]))
Gaussian6 = Gaussian(r, *np.concatenate([[w[5]],popt[15:18]]))
Gaussian7 = Gaussian(r, *np.concatenate([[w[6]],popt[18:21]]))


plt.plot(r, Gaussian1, 'pink', label = 'Co-V')
plt.plot(r, Gaussian2, 'y', label = 'Co-Zr')
plt.plot(r, Gaussian3, 'g', label = 'Co-Co')
plt.plot(r, Gaussian4, 'b', label = 'V-Zr')
plt.plot(r, Gaussian5, 'purple', label = 'V-V')
plt.plot(r, Gaussian6, 'orange', label = 'Zr-Zr')
plt.plot(r, Gaussian7, '--r', label = 'Si-Si')



plt.plot(r, Gaussian1, 'pink')
plt.plot(r, Gaussian2, 'y')
plt.plot(r, Gaussian3, 'g')
plt.plot(r, Gaussian4, 'b')
plt.plot(r, Gaussian5, 'purple')
plt.plot(r, Gaussian6, 'orange')
plt.plot(r, Gaussian7, '--r')

plt.plot(r, fit, 'r', linewidth = 2.0, label = 'fit')

plt.plot(r, Tr-fit, 'black', linewidth = 2.0, label = 'intensity difference')

plt.xlim((1.8, 3.6))
plt.ylim((-0.5, 8.5))
plt.legend()
plt.xlabel('r')
plt.ylabel('T(r)')



def cn(c, a, rij, sigma):
    """
    calculating coordination number according to eq(3) in Ma's paper
    """
    return c*a*(rij+sigma/np.sqrt(2*np.pi))    
    
i = 0
cn_Co_V = cn(0.38, popt[i+1], popt[i], popt[i+2])
cn_V_Co = cn(0.45, popt[i+1], popt[i], popt[i+2])
i = 3
cn_Co_Zr = cn(0.17, popt[i+1], popt[i], popt[i+2])
cn_Zr_Co = cn(0.45, popt[i+1], popt[i], popt[i+2])
i = 6
cn_Co_Co = cn(0.45, popt[i+1], popt[i], popt[i+2])
i = 9
cn_V_Zr = cn(0.17, popt[i+1], popt[i], popt[i+2])
cn_Zr_V = cn(0.38, popt[i+1], popt[i], popt[i+2])
i = 12
cn_V_V = cn(0.38, popt[i+1], popt[i], popt[i+2])
i = 15
cn_Zr_Zr = cn(0.17, popt[i+1], popt[i], popt[i+2])


# result reporting
print "Co-V coordinatin number is:", cn_Co_V
print "V-Co coordinatin number is:", cn_V_Co
print "Co-Zr coordinatin number is:", cn_Co_Zr
print "Zr-Co coordinatin number is:", cn_Zr_Co
print "Co-Co coordinatin number is:", cn_Co_Co
print "V-Zr coordinatin number is:", cn_V_Zr
print "Zr-V coordinatin number is:", cn_Zr_V
print "V-V coordinatin number is:", cn_V_V
print "Zr-Zr coordinatin number is:", cn_Zr_Zr
print '\n'
print "Co-V bond length is:", popt[0]
print "Co-Zr bond length is:", popt[3]
print "Co-Co bond length is:", popt[6]
print "V-Zr bond length is:", popt[9]
print "V-V bond length is:", popt[12]
print "Zr-Zr bond length is:", popt[15]
print "Si-Si bond length is:", popt[18]
print '\n'
print "Co is surrounded by", cn_Co_V + cn_Co_Co + cn_Co_Zr, "atoms"
print "V is surrounded by", cn_V_V + cn_V_Co + cn_V_Zr, "atoms"
print "Zr is surrounded by", cn_Zr_V + cn_Zr_Co + cn_Zr_Zr, "atoms"
    