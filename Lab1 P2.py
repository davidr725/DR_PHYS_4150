# In[2]:

import argparse

parser2 = argparse.ArgumentParser(description="Parses my second problem.")
parser2.add_argument('x0',type=float,help="Distance traveled in light years")
parser2.add_argument('v',type=float,help="What is the speed the spaceship travels at relative to c values 0-1")
args2=parser2.parse_args()

# In[1]:


print("Problem 2")


# In[ ]:


import math

#Ask user for distance
x0 = args2.x0

#Ask user for velocity 
v = args2.v

#Lorentz Factor
gamma = 1/(math.sqrt(1-v**2))

#Dialated Distance
x1 = x0/gamma

#Delta t = distance / velocity
earth_time = (x0/v)
spaceship_time = (x1/v)
print(str("{:.3f}".format(earth_time) + " Light Years"))
print(str("{:.3f}".format(spaceship_time) + " Light Years"))


