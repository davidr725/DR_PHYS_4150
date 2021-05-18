import numpy as np
import matplotlib.pyplot as plt
from vpython import vector
from vpython import arrow
from vpython import color
from vpython import sphere
from vpython import rate


# Author: David Ramirez - 5/18/21
# Based on "Visualizing the Rotation of an Asymmetric Object"
# By: Andrea Ferroglia


'''
===========================
        FUNCTIONS
===========================
'''


# Euler's Equations as first order ODEs
def Euler_EQs(r, t):
    omega1 = r[0]
    omega2 = r[1]
    omega3 = r[2]
    d_omega1 = ((I2 - I3)*omega2*omega3)/(I1)
    d_omega2 = ((I3 - I1)*omega1*omega3)/(I2)
    d_omega3 = ((I1 - I2)*omega1*omega2)/(I3)
    return np.array([d_omega1, d_omega2, d_omega3])


# ODE using Runge Kutta for Euler's Equations
def Euler_Solver(ODE):
    omega1_points = []
    omega2_points = []
    omega3_points = []
    tpoints = np.arange(a, b, h)
    r = np.array([omega1_initial, omega2_initial, omega3_initial], float)

    # Loop to calculate the ODE
    for t in tpoints:
        omega1_points.append(r[0])
        omega2_points.append(r[1])
        omega3_points.append(r[2])
        k1 = h*ODE(r, t)
        k2 = h*ODE(r + .5*k1, t + .5*h)
        k3 = h*ODE(r + .5*k2, t + .5*h)
        k4 = h*ODE(r + k3, t+h)
        r += (k1 + 2*k2 + 2*k3 + k4) / 6

    return omega1_points, omega2_points, omega3_points, tpoints


'''
===========================
    SETUP & COMPUTATION
===========================
'''

# Allow the user to set specific initial conditions
print("Choose a set of initial angular velocities, omega")
print("")
print("Option 1: omega1 = 1, omega2 = .2, omega3 = .01")
print("Option 2: omega1 = .2, omega2 = 1, omega3 = .01")
print("Option 3: omega1 = 1e-8, omega2 = 1e-4, omega3 = .1")
print("")
print("type '1', '2', or '3' to select one of the corresponding options")
choice = int(input())

while choice != 1 and choice != 2 and choice != 3:
    print("invalid selection, please try again")
    print("type '1', '2', or '3' to select one of the corresponding options")
    choice = int(input())

if choice == 1:
    omega1_initial = 1
    omega2_initial = .2
    omega3_initial = .01

elif choice == 2:
    omega1_initial = .2
    omega2_initial = 1
    omega3_initial = .01

elif choice == 3:
    omega1_initial = 1e-8
    omega2_initial = 1e-4
    omega3_initial = 1

# Initial moments of interia, lamda1, lamda2, lamda3
I1 = 3
I2 = 1
I3 = 2


# Runge Kutta setup
a = 0
b = 120
N = 5000
h = (b-a)/N


# setup 3 arrays for x,y,z that store omega(t) values
# Each element in their respective arrays represents omega + dt
omega1_arr, omega2_arr, omega3_arr, time_arr = Euler_Solver(Euler_EQs)
omega1_arr = np.array(omega1_arr)
omega2_arr = np.array(omega2_arr)
omega3_arr = np.array(omega3_arr)

# Calculate the Angular Momentum per component
L1 = I1*omega1_arr
L2 = I2*omega2_arr
L3 = I3*omega3_arr


# Calculate the Rotational Kinetic Energy
L_mag = np.sqrt((I1**2)*(omega1_initial**2) +
                (I2**2)*(omega2_initial**2) +
                (I3**2)*(omega3_initial**2))


# Calculate the Rotational Kinetic Energy
KE = (.5*(I1)*(omega1_initial**2) +
      .5*(I2)*(omega2_initial**2) +
      .5*(I3)*(omega3_initial**2))


# Create an Ellipsoid that shows that the Rotational KE is conserved
coefficents = (.5*(I1/KE), .5*(I2/KE), .5*(I3/KE))
rx, ry, rz = 1/np.sqrt(coefficents)
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x2 = rx * np.outer(np.cos(u), np.sin(v))
y2 = ry * np.outer(np.sin(u), np.sin(v))
z2 = rz * np.outer(np.ones_like(u), np.cos(v))


# Create an Ellipsoid that shows that the Angular Momentum is conserved
coefficents = ((I1**2)/(L_mag**2), (I2**2)/(L_mag**2), (I3**2)/(L_mag**2))
rx, ry, rz = 1/np.sqrt(coefficents)
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x3 = rx * np.outer(np.cos(u), np.sin(v))
y3 = ry * np.outer(np.sin(u), np.sin(v))
z3 = rz * np.outer(np.ones_like(u), np.cos(v))


# Create Unit vectors in the direction of the angular momentum
L1_hat = (I1*omega1_arr)/(L_mag)
L2_hat = (I2*omega2_arr)/(L_mag)
L3_hat = (I3*omega3_arr)/(L_mag)


# Create the unit vectors ei
e1x = 1 + ((L1_hat**2)/(L3_hat - 1))
e1y = (L1_hat*L2_hat)/(L3_hat-1)
e1z = L1_hat

e3x = L1_hat
e3y = L2_hat
e3z = L3_hat

e2x = (e3y*e1z) - (e3z*e1y)
e2y = (-e3x*e1z) + (e3z*e1x)
e2z = (e3x*e1y) - (e3y*e1x)


'''
===========================
       VISUALIZATION
===========================
'''


# Show the behavior of the angular velocities with respect to time
# Angular Velocity Omega(t) vs Time
plt.plot(time_arr, omega1_arr, label='omega 1', color='red')
plt.plot(time_arr, omega2_arr, label='omega 2', color='blue')
plt.plot(time_arr, omega3_arr, label='omega 3', color='green')
plt.legend()
plt.show()


# Plot the Ellipsoids of KE & L and plot their intersection
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax1.plot_surface(x2, y2, z2, rstride=10, cstride=10,
                 cmap='Blues', edgecolor='none')
ax1.plot_surface(x3, y3, z3, rstride=10, cstride=10,
                 cmap='viridis', edgecolor='none')
ax1.plot(omega1_arr, omega2_arr, omega3_arr, color='red')
ax1.set_xlim(-1, 1)
ax1.set_ylim(-1, 1)
ax1.set_zlim(-1, 1)
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.show()


'''
===========================
        ANIMATION
===========================
'''

origin = vector(0, 0, 0)

arrow_e1 = arrow(pos=origin, axis=vector(e1x[0], e1y[0], e1z[0]),
                 color=color.red)
arrow_e2 = arrow(pos=origin, axis=vector(e2x[0], e2y[0], e2z[0]),
                 color=color.blue)
arrow_e3 = arrow(pos=origin, axis=vector(e3x[0], e3y[0], e3z[0]),
                 color=color.green)

# Axis
x_axis1 = arrow(pos=origin, axis=vector(1, 0, 0), color=color.white)
y_axis1 = arrow(pos=origin, axis=vector(0, 1, 0), color=color.white)
z_axis1 = arrow(pos=origin, axis=vector(0, 0, 1), color=color.white)
x_axis2 = arrow(pos=origin, axis=vector(-1, 0, 0), color=color.white)
y_axis2 = arrow(pos=origin, axis=vector(0, -1, 0), color=color.white)
z_axis2 = arrow(pos=origin, axis=vector(0, 0, -1), color=color.white)

i = 0
while i < N:
    rate(30)
    r1 = vector(e1x[i], e1y[i], e1z[i])
    r2 = vector(e2x[i], e2y[i], e2z[i])
    r3 = vector(e3x[i], e3y[i], e3z[i])
    tip1 = sphere(pos=vector(e1x[i], e1y[i], e1z[i]),
                  radius=.05, color=color.red)
    tip2 = sphere(pos=vector(e2x[i], e2y[i], e2z[i]),
                  radius=.05, color=color.blue)
    tip3 = sphere(pos=vector(e3x[i], e3y[i], e3z[i]),
                  radius=.05, color=color.green)
    i += 1
    arrow_e1.axis = r1
    arrow_e2.axis = r2
    arrow_e3.axis = r3
