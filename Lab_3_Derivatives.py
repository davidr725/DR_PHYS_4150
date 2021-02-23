# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:07:34 2021

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x*(x-1)

n = 1
list = [1e-2,1e-4,1e-6,1e-8,1e-10,1e-12,1e-14]
delta_array = np.array(list)
derivatives = np.zeros(7)


for i in range(0,7):
    derivatives[i] = (f(n + delta_array[i]) - f(n))/(delta_array[i])
    
print("The derivative values for the function are: ") 
print(derivatives)

derivatives = abs(derivatives - 1)

print('\n')   
print("The error values for the function are: ")
print(derivatives)

plt.loglog(delta_array,derivatives)
plt.ylabel('derivative values')
plt.xlabel(r'$\delta$ values')
plt.show()
