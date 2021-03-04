# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:34:32 2021

@author: david
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as constants

def r(x,y):
    return np.sqrt(x**2 + y**2)

#Setting up the grid
x_0, x_1 = -50,50
y_0, y_1 = -50,50
x = np.linspace(x_0, x_1,100)
y = np.linspace(y_0, y_1,100)
x_grid, y_grid = np.meshgrid(x, y)

#Placing the particles on the grid
Point_1 = np.array([-5,0])
Point_2 = np.array([5,0])

#Calcuating distance R to the particles for every point on the grid
Point_1X, Point_1Y = Point_1[0] , Point_1[1] 
Point_2X, Point_2Y = Point_2[0] , Point_2[1] 

#Calculate the potential for each point
x1 , y1 = x_grid - Point_1X , y_grid - Point_1Y
x2 , y2 = x_grid - Point_2X , y_grid - Point_2Y

#plot of the electric potential
C = 1/(4*np.pi*constants.epsilon_0)
v1 = (1)*C*(1/r(x1,y1))
v2 = (-1)*C*(1/r(x2,y2))
v_total = v1 + v2
plt.imshow(v_total)
plt.title("Electric potential of two particles")
plt.show()

#Take the partial deriviative numerically to determine the electric field
h = 1e-5
def v(q,x,y):
    return q*C*(1/r(x,y))
vx1_prime = (v(1,(x1+h/2),y1) - v(1,(x1-h/2),y1))/h
vy1_prime = (v(1,x1,(y1+h/2)) - v(1,x1,(y1-h/2)))/h
vx2_prime = (v(-1,(x2+h/2),y2) - v(-1,(x2-h/2),y2))/h
vy2_prime = (v(-1,x2,(y2+h/2)) - v(-1,x2,(y2-h/2)))/h
VX_prime = vx1_prime + vx2_prime
VY_prime = vy1_prime + vy2_prime

#1m x 1m plot
plt.streamplot(x_grid,y_grid,VX_prime,VY_prime, density=2.5,linewidth=.5,arrowsize=.8)
plt.title("E Field of a Dipole")
plt.xlabel("centimeters")
plt.ylabel("centimeters")
plt.show()
 
#Zoomed in plot, left it as a comment because it takes about 30-45 seconds to load due to the density
plt.streamplot(x_grid,y_grid,VX_prime,VY_prime, density=8,linewidth=.5,arrowsize=1.2)
plt.title("E Field of a Dipole (Zoomed in)")
plt.xlabel("centimeters")
plt.ylabel("centimeters")
plt.ylim([-10,10])
plt.xlim([-10,10])
plt.show()





