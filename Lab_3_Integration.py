# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 14:04:35 2021

@author: david
"""

import numpy as np

#define integrand
def f(x):
    return np.sqrt(1-x**2)  

#define reimann sum
def I(N):
    h = 2/N
    total = 0
    for k in range(1,N):
        x_k = -1 + (h*k)
        total += h*f(x_k)
    print("The value for the Reimann Sum with " +str(N) + " slices is: " +str(total))

#print for values of N
I(10)
I(100)
I(1000)
I(10000)