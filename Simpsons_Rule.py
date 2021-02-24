# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:40:53 2021

@author: david
"""

def f(x):
    return x**4 - 2*x + 1

N = 1000
b = 2
a = 0
h = (b-a)/N

odd = 0
for k in range(1,N,2):
    odd += f(a + k*h)
    
even = 0
for k in range (2,N,2):
    even += f(a + k*h)
    
I = (1/3) * h * (f(a) + f(b) + 4*odd + 2*even)
print("The area calculated by Simpson's Rule is: " + str(I))
    
def f_3prime(x):
    return 24*x

E = -1/90*(h**4)*(f_3prime(a) - f_3prime(b))
print("The error calculated by the Euler-Maclaurin formula is: " + str(E))