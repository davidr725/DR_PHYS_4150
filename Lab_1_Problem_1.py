#!/usr/bin/env python
# coding: utf-8

# In[1]:


import argparse

parser = argparse.ArgumentParser(description="Parses my Code.")
parser.add_argument('h',type=float,help="height of the object")
args=parser.parse_args()

# In[2]:


print("Problem 1")


# In[3]:


import math

#Acceleration due to Gravity
g = 9.8

#Height Inputted by User
h = args.h

#Calculation of Time it takes to hit the ground
t = math.sqrt((2*h)/g)

#Print the output in a clean way
print(str("{:.3f}".format(t)) + " seconds")


# In[2]:


parser.add_argument('x0',type=float,help="Distance traveled in light years")


# In[1]:


print("Problem 2")


# In[ ]:


import math

#Ask user for distance
x0 = args.x0

#Ask user for velocity
v = float(input("What is the speed that the spaceship is traveling in terms of c: "))

#Lorentz Factor
gamma = 1/(math.sqrt(1-v**2))

#Dialated Distance
x1 = x0/gamma

#Delta t = distance / velocity
earth_time = (x0/v)
spaceship_time = (x1/v)
print(str("{:.3f}".format(earth_time) + " Light Years"))
print(str("{:.3f}".format(spaceship_time) + " Light Years"))


# In[ ]:




