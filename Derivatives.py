# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:25:15 2021

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt

#Numerical derivative
def f(x):
    return 1 + .5 * np.tanh(2*x)

n = np.linspace(-2,2,100)
h = 1e-5

f_prime = (f(n + h/2) - f(n - h/2))/h
#print(f_prime)


#Analytical derivative 
def g(x):
    return 1/(np.cosh(2*x)**2)

p = np.linspace(-2,2,100)

#print(g(p))

#Plot Analytic vs Numerical
plt.title("Numerical vs Analytical Derivative with Central Difference")

plt.plot(n, f_prime)
plt.scatter(p, g(p))
plt.show()
