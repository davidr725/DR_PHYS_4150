# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:47:20 2021

@author: david
"""

import numpy as np
import gaussxw as gs

def h(x):
    return x**4 - (2*x) + 1

n = 10
a = 0
b = 2

#Get weights and points from gaussXW function
points, weights = gs.gaussxwab(n, a, b)

#Use Formula Summation Wk*f(xk) 
answer = weights*h(points)
answer = np.sum(answer)

#Print the answer
print(answer)



    
    



    




