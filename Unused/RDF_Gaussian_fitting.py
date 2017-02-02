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
    RDF = np.zeros_like(r)
    for i in range(0, len(params), 3):
        rij = params[i]
        a = params[i+1]
        sigma = params[i+2]
        RDF = RDF + a/(np.sqrt(2*np.pi)*sigma) * np.exp( -((r - rij)**2/(2*sigma**2))) 
    return RDF
    
    
def Gaussian(r, *param):
    """
    for plotting Gaussian curve for each M-M pair. param is an array of lenth 4
    """
    Tr = np.zeros_like(r)
    rij = param[0]
    a = param[1]
    sigma = param[2]
    Tr = Tr + a/(np.sqrt(2*np.pi)*sigma) * np.exp( -((r - rij)**2/(2*sigma**2)))
    return Tr


# initialization 
guess = [2.59,1,0.1,2.85,1,0.1,2.50,0,0.1,2.94,1,0.1,2.68,0,0.1,3.4,0,0.1,2.03,1,0.1]

# setting constraint
low = (2.54,0,0,2.8,0,0,2.45,0,0,2.89,0,0,2.63,0,0,3.15,0,0,2.01,0,0)
high = (2.64,20,0.2,2.9,20,0.2,2.55,20,0.2,2.99,20,0.2,2.73,20,0.2,3.5,20,0.2,2.05,20,0.2)


path = 'C:\Research_FangRen\Publications\Combinatorial Search for Metallic Glasses in Co-V-Zr ternary systems\MG\\'

filename = 'PDF_r_G(r).csv'
fullname = path + filename
#
#
####################
### Unannealed sample
####################
#
#data = np.genfromtxt(fullname, delimiter=',', skip_header = 2)
#r = data[175:360,0]
#Gr = data[175:360,1]
#gr = Gr +1
#
#RDF = 4 *np.pi*0.068*gr*(r**2)
#
#
#plt.plot(r,RDF, 'o', label = 'unannealed PDF')
#
#
##
##initial_guess = func(r, *guess)
##plt.plot(r, initial_guess)
#

###################
## annealed sample
###################
data = np.genfromtxt(fullname, delimiter=',', skip_header = 2)
r = data[175:360,2]
Gr = data[175:360,3]
gr = Gr +1

#RDF = 4 *np.pi*0.068*gr*r**2
RDF = 4 *np.pi*0.05*gr*r**2

plt.plot(r,RDF, 'o', label = 'annealed PDF')
#plt.plot(r, background)
#plt.plot(r, Tr-background)

#initial_guess = func(r, *guess)
#plt.plot(r, initial_guess)

#

##################
# start fitting
##################

popt, pcov = curve_fit(func, r, RDF, p0=guess, bounds = (low, high))
fit = func(r, *popt)

Gaussian1 = Gaussian(r, *popt[:3])
Gaussian2 = Gaussian(r, *popt[3:6])
Gaussian3 = Gaussian(r, *popt[6:9])
Gaussian4 = Gaussian(r, *popt[9:12])
Gaussian5 = Gaussian(r, *popt[12:15])
Gaussian6 = Gaussian(r, *popt[15:18])
Gaussian7 = Gaussian(r, *popt[18:21])

plt.plot(r, Gaussian1, 'pink', label = 'Co-V')
plt.plot(r, Gaussian2, 'y', label = 'Co-Zr')
plt.plot(r, Gaussian3, 'g', label = 'Co-Co')
plt.plot(r, Gaussian4, 'b', label = 'V-Zr')
plt.plot(r, Gaussian5, 'purple', label = 'V-V')
plt.plot(r, Gaussian6, 'orange', label = 'Zr-Zr')
plt.plot(r, Gaussian7, '--r', label = 'Si-Si')

#
#plt.plot(r, Gaussian1, 'pink')
#plt.plot(r, Gaussian2, 'y')
#plt.plot(r, Gaussian3, 'g')
#plt.plot(r, Gaussian4, 'b')
#plt.plot(r, Gaussian5, 'purple')
#plt.plot(r, Gaussian6, 'orange')
#plt.plot(r, Gaussian7, '--r')
#
plt.plot(r, fit, 'r', linewidth = 2.0, label = 'fit')

plt.plot(r, RDF-fit, 'black', linewidth = 2.0, label = 'intensity difference')

plt.xlim((1.8, 3.6))
plt.ylim((-0.5, 25))
plt.legend()
plt.xlabel('r')
plt.ylabel('RDF')


#
#def cn(c, a, rij, sigma):
#    """
#    calculating coordination number according to eq(3) in Ma's paper
#    """
#    return c*a*(rij+sigma/np.sqrt(2*np.pi))    
#    
#i = 0
#cn_Co_V = cn(0.38, popt[i+1], popt[i], popt[i+2])
#cn_V_Co = cn(0.45, popt[i+1], popt[i], popt[i+2])
#i = 3
#cn_Co_Zr = cn(0.17, popt[i+1], popt[i], popt[i+2])
#cn_Zr_Co = cn(0.45, popt[i+1], popt[i], popt[i+2])
#i = 6
#cn_Co_Co = cn(0.45, popt[i+1], popt[i], popt[i+2])
#i = 9
#cn_V_Zr = cn(0.17, popt[i+1], popt[i], popt[i+2])
#cn_Zr_V = cn(0.38, popt[i+1], popt[i], popt[i+2])
#i = 12
#cn_V_V = cn(0.38, popt[i+1], popt[i], popt[i+2])
#i = 15
#cn_Zr_Zr = cn(0.17, popt[i+1], popt[i], popt[i+2])
#
#
## result reporting
#print "Co-V coordinatin number is:", cn_Co_V
#print "V-Co coordinatin number is:", cn_V_Co
#print "Co-Zr coordinatin number is:", cn_Co_Zr
#print "Zr-Co coordinatin number is:", cn_Zr_Co
#print "Co-Co coordinatin number is:", cn_Co_Co
#print "V-Zr coordinatin number is:", cn_V_Zr
#print "Zr-V coordinatin number is:", cn_Zr_V
#print "V-V coordinatin number is:", cn_V_V
#print "Zr-Zr coordinatin number is:", cn_Zr_Zr
#print '\n'
print "Co-V bond length is:", popt[0]
print "Co-Zr bond length is:", popt[3]
print "Co-Co bond length is:", popt[6]
print "V-Zr bond length is:", popt[9]
print "V-V bond length is:", popt[12]
print "Zr-Zr bond length is:", popt[15]
print "Si-Si bond length is:", popt[18]
print '\n'
print "Co-V pair number is:", popt[1]
print "Co-Zr pair number is:", popt[4]
print "Co-Co pair number is:", popt[7]
print "V-Zr pair number is:", popt[10]
print "V-V pair number is:", popt[13]
print "Zr-Zr pair number is:", popt[16]
print "Si-Si pair number is:", popt[19]


    