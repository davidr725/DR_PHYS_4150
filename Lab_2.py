#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[42]:


def deltoid():
    theta = np.radians(np.linspace(0,360,500))
    x = 2*np.cos(theta) + np.cos(2*theta)
    y = 2*np.sin(theta) - np.sin(2*theta)
    plt.plot(x,y)
    plt.ylabel('deltoid curve')
    plt.show()
    return [x,y]
    
x,y = deltoid()


# In[39]:


def spiral():
    thetaB = np.radians(np.linspace(0,1800,500))
    r = (thetaB)**2
    xB = r*np.cos(thetaB)
    yB = r*np.sin(thetaB)
    plt.plot(xB,yB)
    plt.ylabel('Galilean Spiral')
    plt.show()
    return xB,yB

xB, yB = spiral()


# In[40]:


def Feys():
    thetaC = np.radians(np.linspace(0,4320,2000))
    r = np.exp(np.cos(thetaC)) - (2*np.cos(4*thetaC)) + (np.sin(thetaC/12)**5)
    xC = r*np.cos(thetaC)
    yC = r*np.sin(thetaC)
    plt.plot(xC,yC)
    plt.ylabel("Fey's Function")
    plt.show()
    return xC, yC

xC, yC = Feys()


# In[50]:


fig, axs = plt.subplots(3,figsize=[6,12])

axs[0].plot(x,y)
axs[0].set_title('Deltoid Curve')
axs[1].plot(xB,yB)
axs[1].set_title("Galilean Spiral")
axs[2].plot(xC,yC)
axs[2].set_title("Fey's Function")
plt.show()


# In[ ]:




