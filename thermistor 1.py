# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 00:07:48 2020

@author: anntara
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#importing data
T, T_unc, R, R_unc = np.loadtxt("thermistor data.txt", comments="#", skiprows=2, unpack = True)

#Switch Temp to Kelvin and Resitance to Ohm
T = T + 273
R = R * 1000

# Steinhart-Hart Equation
def SH(x, a1, a2, a3, a4):
    return 1 / (a1 + a2 * np.log(x) + a3 * np.power(np.log(x),2) + a4 * np.power(np.log(x),3))

# degrees of freedom for reduced chi squared
ddof = np.size(T) - 1	

#fitting data    
popt, pcov = curve_fit(SH, R, T, p0=[1e-4, 1e-4, 1e-4, 1e-4])

#printing the result
print("The value of a1, a2, a3 and, a4 are the following; {}".format(popt))
print ("The uncertainity of the coefficients would be;", np.sqrt(pcov[0, 0]))

#goodness of the fit
Chi = T - SH(R, *popt)
Chi_sqr = np.sum((Chi / T_unc) ** 2)
print ("Reduced chi squared is;", Chi_sqr / ddof)

#defining a fuction that can find the temperature using resitance
def Temp(x):
    return 1 / (popt[0] + popt[1] * np.log(x) + popt[2] * np.power(np.log(x),2) + popt[3] * np.power(np.log(x),3))

#temperaature measured from the given data
T2 = Temp(R)

# plot data
plt.plot(R, T)
plt.plot(R, T2)
plt.title("Resitance VS Time")
plt.xlabel("Resistance (kOhm)")
plt.ylabel("Temperature (K)")
plt.savefig("Resitance VS Time.png") 
plt.show()

#inputing a Resitance with return the corresponsing Temperature in DegC
def main():
    Resistance = float(input("Insert Resitnce in Ohm: "))
    TempC = Temp(Resistance) - 273
    
    print("For this resistance the corresponding temperature is: ", TempC, " degC")
    
main()