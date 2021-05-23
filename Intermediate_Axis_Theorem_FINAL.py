import numpy as np
import matplotlib.pyplot as plt
import vpython as vp


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
    '''
    ---------------------Euler_EQs------------------------
    The set of coupled differential Euler's equations for
    rotational mechanics in 3 dimensions

    r = an array of angular velocities omega
    t = time array
    '''
    omega1 = r[0]
    omega2 = r[1]
    omega3 = r[2]
    d_omega1 = ((I2 - I3)*omega2*omega3)/(I1)
    d_omega2 = ((I3 - I1)*omega1*omega3)/(I2)
    d_omega3 = ((I1 - I2)*omega1*omega2)/(I3)
    return np.array([d_omega1, d_omega2, d_omega3])


# ODE using Runge Kutta for Euler's Equations
def Euler_Solver(ODE):
    '''
    ---------------------Euler_Solver------------------------
    Takes the Euler_EQs function and returns a value
    for each respective omega (Angular Velocity)
    for each instance in time as an array of values

    ODE = Euler_EQs function

    Solves the ODE with 4th order Runge Kutta

    Returns 4 arrays, 1 Omega value for each axis and
    an array that stores all the time increments
    '''

    # Setup
    omega1_points = []
    omega2_points = []
    omega3_points = []
    tpoints = np.arange(a, b, h)
    r = np.array([omega1_initial, omega2_initial, omega3_initial], float)

    # Runge Kutta
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
      USER INPUT SETUP
===========================

Allow the user to choose from a pre-defined
set of initial conditions at initialization
'''

print("Choose a set of initial angular velocities, omega")
print("")
print("Option 1: omega1 = 1, omega2 = .2, omega3 = .01")
print("Option 2: omega1 = .2, omega2 = 1, omega3 = .01")
print("Option 3: omega1 = 1e-8, omega2 = 1e-4, omega3 = 1")
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


'''
===========================
   PHYSICS & COMPUTATION
===========================
'''


# Initial moments of interia, lamda1, lamda2, lamda3
I1 = 3
I2 = 1
I3 = 2


# Runge Kutta setup
a = 0
b = 150
N = 10000
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


# Calculate the Angular Momentum
L_mag = np.sqrt((I1**2)*(omega1_initial**2) +
                (I2**2)*(omega2_initial**2) +
                (I3**2)*(omega3_initial**2))


# Calculate the Rotational Kinetic Energy
KE = (.5*(I1)*(omega1_initial**2) +
      .5*(I2)*(omega2_initial**2) +
      .5*(I3)*(omega3_initial**2))


# Create an Ellipsoid that shows that the Rotational KE is conserved
coefficents = (.5*(I1/KE), .5*(I2/KE), .5*(I3/KE))
KEx, KEy, KEz = 1/np.sqrt(coefficents)


# Create an Ellipsoid that shows that the Angular Momentum is conserved
coefficents = ((I1**2)/(L_mag**2), (I2**2)/(L_mag**2), (I3**2)/(L_mag**2))
Lx, Ly, Lz = 1/np.sqrt(coefficents)


# Create Unit vectors in the direction of the angular momentum
L1_hat = (I1*omega1_arr)/(L_mag)
L2_hat = (I2*omega2_arr)/(L_mag)
L3_hat = (I3*omega3_arr)/(L_mag)


# Create the principle axis's of the object
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

Plot 1: Relationships between the Angular Velocities
and time

Plot 2: Visualization of how the Kinetic Energy Ellipsoid
and Angular Momentum Ellipsoid overlap and intersect

'''

# Plot 1: Matplotlib graph
# Show the behavior of the angular velocities with respect to time
# Angular Velocity Omega(t) vs Time
plt.plot(time_arr, omega1_arr, label='omega 1', color='red')
plt.plot(time_arr, omega2_arr, label='omega 2', color='blue')
plt.plot(time_arr, omega3_arr, label='omega 3', color='green')
plt.title('Angular Velocity $\omega$ vs Time')
plt.xlabel('Time')
plt.ylabel('$\omega$')
plt.legend()
plt.show()


# Plot 2: Ellipsoids
origin = vp.vector(0, 0, 0)
scene1 = vp.canvas(title='Ellipsoids', width=800, height=800,
                   center=origin)

# Create a set of Axis & Label each Axis
x_axis = vp.cylinder(pos=origin, axis=vp.vector(1.2, 0, 0), radius=.02,
                     color=vp.color.yellow, opacity=.5)
y_axis = vp.cylinder(pos=origin, axis=vp.vector(0, 1.2, 0), radius=.02,
                     color=vp.color.yellow, opacity=.5)
z_axis = vp.cylinder(pos=origin, axis=vp.vector(0, 0, 1.2), radius=.02,
                     color=vp.color.yellow, opacity=.5)
lx_text = vp.text(text='lx', pos=vp.vector(1.1, .1, 0), align='center',
                  height=0.05, color=vp.color.white, billboard=True,
                  emissive=True)
ly_text = vp.text(text='ly', pos=vp.vector(.1, 1.1, 0), align='center',
                  height=0.05, color=vp.color.white, billboard=True,
                  emissive=True)
lz_text = vp.text(text='lz', pos=vp.vector(-.1, 0, 1.1), align='center',
                  height=0.05, color=vp.color.white, billboard=True,
                  emissive=True)


# Legend for the Ellipsoids visualization
KE_text = vp.text(text='KE', pos=vp.vector(1.3, .5, 0),
                  align='center', height=.05, color=vp.color.orange,
                  billboard=True, emissive=True)
L_text = vp.text(text='ω', pos=vp.vector(1.3, 0, 0),
                 align='center', height=.05, color=vp.color.blue,
                 billboard=True, emissive=True)


# Create the Ellipsoids
L_ELL = vp.sphere(pos=origin, size=vp.vector(Lx, Ly, Lz),
                  color=vp.color.blue, opacity=.8)
KE_ELL = vp.sphere(pos=origin, size=vp.vector(KEx, KEy, KEz),
                   color=vp.color.orange, opacity=.8)


'''
===========================
        ANIMATION
===========================

Animation of the rotation of the unit vectors eij
using Vpython.
'''

scene2 = vp.canvas(title='Animation', width=800, height=800,
                   center=origin)


# Create a set of Axis & Label each Axis
x_axis = vp.cylinder(pos=origin, axis=vp.vector(1, 0, 0), radius=.02,
                     color=vp.color.yellow, opacity=.5)
y_axis = vp.cylinder(pos=origin, axis=vp.vector(0, 1, 0), radius=.02,
                     color=vp.color.yellow, opacity=.5)
z_axis = vp.cylinder(pos=origin, axis=vp.vector(0, 0, 1), radius=.02,
                     color=vp.color.yellow, opacity=.5)

x_text = vp.text(text='X', pos=vp.vector(1.1, 0, 0), align='center',
                 height=0.05, color=vp.color.white, billboard=True,
                 emissive=True)
y_text = vp.text(text='Y', pos=vp.vector(0, 1.1, 0), align='center',
                 height=0.05, color=vp.color.white, billboard=True,
                 emissive=True)
z_text = vp.text(text='Z', pos=vp.vector(0, 0, 1.1), align='center',
                 height=0.05, color=vp.color.white, billboard=True,
                 emissive=True)


# Create vectors that update for each frame using the stored values
arrow_e1 = vp.arrow(pos=origin, axis=vp.vector(e1x[0], e1y[0], e1z[0]),
                    color=vp.color.red)
arrow_e2 = vp.arrow(pos=origin, axis=vp.vector(e2x[0], e2y[0], e2z[0]),
                    color=vp.color.blue)
arrow_e3 = vp.arrow(pos=origin, axis=vp.vector(e3x[0], e3y[0], e3z[0]),
                    color=vp.color.green)


# Loop that animates the frames
for i in range(1, N, 5):
    vp.rate(30)
    r1 = vp.vector(e1x[i], e1y[i], e1z[i])
    r2 = vp.vector(e2x[i], e2y[i], e2z[i])
    r3 = vp.vector(e3x[i], e3y[i], e3z[i])

    path_e1 = vp.sphere(pos=r1, radius=.01, color=vp.color.red)
    path_e2 = vp.sphere(pos=r2, radius=.01, color=vp.color.blue)
    path_e3 = vp.sphere(pos=r3, radius=.01, color=vp.color.green)

    arrow_e1.axis = r1
    arrow_e2.axis = r2
    arrow_e3.axis = r3
