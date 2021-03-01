# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:41:53 2021

@author: david
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x,c):
    return 1-np.exp(-c*x)

y = f(1,2)
while y - f(y,2) > 1e-10:
    y = f(y,2)
    
print("When c is 2 the solution to the problem is: " + str(y))    


#relaxation for a range of C values    
c = np.arange(0,3.1,.1,dtype=float)
n = len(c)
y = f(1,c)


for i in range(0,n):
    while y[i] - f(y[i],c[i]) > 1e-10:
        y[i] = f(y[i],c[i])

print("")
print("When c is in a range from 0-3 the solutions are the following: ")
print(y)



#Check with previous solution 
print("")
print("Check this range of values using previous solution")
print(c[-11])
print(y[-11])

plt.plot(c,y)
plt.title('Relaxation Method for x as a function of c')
plt.xlabel('c values')
plt.ylabel('x values')
plt.show()

