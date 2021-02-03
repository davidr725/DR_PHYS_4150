#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
program_name = sys.argv[0]
h = sys.argv[1]

# In[2]:


print("Problem 1")


# In[3]:


import math

#Acceleration due to Gravity
g = 9.8

#Height Inputted by User
h = float(h)

#Calculation of Time it takes to hit the ground
t = math.sqrt((2*h)/g)

#Print the output in a clean way
print(str("{:.3f}".format(t)) + " seconds")






