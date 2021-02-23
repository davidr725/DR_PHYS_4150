# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 14:32:54 2021

@author: david
"""
#import necessary Libs
import scipy.constants as cons
import numpy as np


#setup argparse for command line
import argparse
parser = argparse.ArgumentParser(description="Parses my problem")
parser.add_argument('slices',type = int,help="number of slices for your integral. Higher values tend to be more accurate")
parser.add_argument('lower_bound',type = float,help="lower limit of your integral.")
parser.add_argument('upper_bound',type = float,help="upper limit of your integral.")
args = parser.parse_args()

while args.lower_bound == 0:
    args.lower_bound = input("you cannot divide by zero, please enter in a small number larger than 0. example: 1e-3. : ")
        
#define the leading term in front of the integral
def f(T):
    leading_term = (cons.k**4)/((4*cons.pi**2)*(cons.c**2)*(cons.hbar**3))
    #print(leading_term)
    return(T**4 * leading_term)

#define the integrand
def g(x):
    return (x**3)/(np.exp(x) - 1)

#define the integral with Simpson's rule
def I(N,a,b):
    h = (b-a)/N
    
    odd = 0
    for k in range(1,N,2):
        odd += g(a + k*h)
    
    even = 0 
    for k in range(2,N,2):
        even += g(a + k*h)
    
    return((1/3)* h* (g(a) + g(b) + 4*odd + 2*even) )


#Define Stefan-Boltzmann Equation
W = f(1) * I(args.slices,args.lower_bound,args.upper_bound)

#Error difference between numerical and analytical
E = abs(cons.Stefan_Boltzmann - W)

#Print my answer vs Stefan-Boltzmann
print("The numerical value you derived for Stefan-Boltzmann's constant is: " + str(W))
print("The analytical value of Stefan-Bolzmann's constant is: " + str(cons.Stefan_Boltzmann))
print("The difference between both values is: " + str(E))
    

#W = f(1) * I(50000,1e-10,100)
