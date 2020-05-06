# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 19:48:19 2020

@author: annta
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#importing data
T, T_unc, R, R_unc = np.loadtxt("thermistor data.txt", comments="#", skiprows=2, unpack = True)

#Switch Temp to Kelvin and Resitance to Ohm
T = T + 273
R = R * 1000
print(R)
# Steinhart-Hart Equation

def SH(x, a1, a2, a3, a4):
    return 1 / (a1 + a2 * np.log(x) + a3 * np.power(np.log(x),2) + a4 * np.power(np.log(x),3))

#fitting data
    
popt, pcov = curve_fit(SH, R, T, p0=[1e-4, 1e-4, 1e-4, 1e-4])

print("The value of a1, a2, a3 and, a4 are the following; {}".format(popt))


def Temp(x):
    return 1 / (popt[0] + popt[1] * np.log(x) + popt[2] * np.power(np.log(x),2) + popt[3] * np.power(np.log(x),3))


T2 = Temp(R)
# plot original data and result

plt.plot(R, T)
plt.plot(R, T2)
plt.title("Resitance VS Time")
plt.xlabel("Resistance (kOhm)")
plt.ylabel("Temperature (K)")
plt.savefig("Resitance VS Time.png") 
plt.show()
'''
def main():
    Resistance = int(input("Insert Resitnce in Ohm: "))
    Temp(Resistance)
    print("For this resistance the corresponding temperature is: ", Temp(Resistance))
    
main()'''