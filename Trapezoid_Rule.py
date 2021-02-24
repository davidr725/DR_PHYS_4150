# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:12:55 2021

@author: david
"""

def f(x):
    return x**4 - 2*x + 1

N = 1000
a = 0
b = 2
h = (b-a)/N #width of a slice
s = .5*f(a) + .5*f(b)

for k in range(1,N):
    s += f(a+k*h)
    
print("The area calculated by the Trapezoid Rule is: " + str(h*s))

def f_prime(x):
    return 4*x**3 - 2

E = 1/12*h**2*(f_prime(a) - f_prime(b))
print("The error calculated by the Euler-Maclaurin formula is: " + str(E))