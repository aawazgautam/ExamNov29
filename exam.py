# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:43:41 2022

@author: Aawaz Gautam 
Lamar ID: L20493942

Submitted to: Dr. Venkatesh Uddameri
"""

#Problem 1.

#Source: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter19.04-Newton-Raphson-Method.html

#importing numpy library 
#import numpy as np

# Defining the constants given in the problem
q  = 40 #cfs
cd = 0.6  # discharge coefficient no unit
pi = 3.14  # constant value
g = 32.2 # ft/s2
constant= 16*q**2/(pi*cd**2*g)

# Function to calculate the functional file.
def fun (d):
    d= d**5 - 12 * d**4 +constant
    return d
# Function to calculate the first derivative.
def fun_fir(d1):
    d1: 5*d1**4 - 48*d1**3 # manually calculated first derivative.
    return d1

"""
newton_raphson = 1.4 - (f(1.4))/(f_prime(1.4))

print("newton_raphson =", newton_raphson)
print("sqrt(2) =", np.sqrt(2))
"""

d1n=0
tol=1 # tolerance defined to enter the loop.
while (tol > 0.0000000001):
        # First we save existing value of x,y&z to a variable and determine the more precise value of.
        d1= d1n
        d1n=d1-fun(d1)/fun_fir(d1)
    
        #Updating the condition value as the maximum of the difference between each present and previous values of each variables
        tol= abs(d1-d1n)
        
print(" The value of diameter is:", d1n,"ft.")
        
 # Problem 2
# Data Source: https://www2.census.gov/programs-surveys/popest/tables/2010-2020/national/totals/NST-EST2020.xlsx       
#Downloaded the census data in xlxs format and saved it as csv.

import pandas as pd # importing library
pop = pd.read_csv("C:\\Users\\aawaz\\Desktop\\exam\\data.csv") # importing the file for plotting

# importing matplotlib library to plot line graph
import matplotlib.pyplot as plt

# Here had to create the list of populations because I wasn't able to read the valued from the excel file somehow.
population=[308745538, 308758105, 309327143, 311583481, 313877662, 316059947, 318386329, 320738994, 323071755, 325122128, 326838199, 328329953, 329398742] 
year =['2010 Apr', '2010 Jul', '2011','2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020 Apr', '2020 Jul']

plt.plot(year, population) # plot x axis vs y axis
plt.ylabel("Population in number")  # label for y axis
plt.title("Population of US 2010-2020")  # Title of the plot
plt.axis(year)
plt.show()  # command to show the plot



# Problem 3 
# Given condition a =L =25000cm
# DEfiening cnsants

# length of the cantilever
l= 25000/100 #m
E= 200000 #pa = N/m2
I= 81960000/pow(100,4) # m4
# deflection due to uniform load:

del_uni= q*l/(8*E*I))
# Plan is to add the deflection due to uniform load and due to point load bu using the given equations












