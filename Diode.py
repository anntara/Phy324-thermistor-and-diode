# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:27:03 2020

@author: anntara
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#importing data
V, V_unc, I, I_unc = np.loadtxt("Diode Data.txt", comments="#", skiprows=2, unpack = True)
                   
#convert to amps
I = I * 0.001
I_unc = I_unc *0.001

# degrees of freedom for reduced chi squared
ddof = np.size(V) - 1	
#print (ddof)


#Shockley equation
def Shockley_Eq (V, X, I0):
    T = 298            #room tempersture in Kelvin
    k = 1.381e-23      #boltzman constant
    q = 1.60e-19
    I2 = I0 * (np.exp( (q * V) / (X * k * T) ) - 1)
    return np.abs(I2)
popt, pcov = curve_fit (Shockley_Eq, V, I)

print ("The value of I0 is: ", popt[0], " A +/- ", np.sqrt(pcov[0, 0]))
print ("The Value of the Boltzmann Constant is: ", popt[1], " +/- ", np.sqrt(pcov[1, 1]))


#goodness of the fit
Chi = I - Shockley_Eq(V, *popt)
Chi_sqr = np.sum((Chi / I_unc) ** 2)
print ("Reduced chi squared is;", Chi_sqr / ddof)

#plotting data
plt.plot (V, I, label = "original")
plt.plot(V, Shockley_Eq(V, *popt), label = "Fitted Curve")
plt.title ("Voltage Vs Current")
plt.xlabel ("Voltage (V)")
plt.ylabel ("Current (mA)")
plt.savefig ("Voltage Vs Current") 
plt.show ()

                       
                               