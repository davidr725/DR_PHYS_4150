###############################################################################
#              VISUALIZING THE ROTATION OF AN ASYMMETRIC OBJECT               #
#                                                                             #
# This code was written to accompany the paper                                #
# "Visualizing the Rotation of an Asymmetric Object"                          #
# (Link to follow)                                                            #
#                                                                             #
# This code was written by David A. Ramirez                                   #
# <david.ramirez4@mail.citytech.cuny.edu>                                     #
#                                                                             #
# ATTN: WIN10 USERS                                                           #
# VPYTHON CAN HANG ON EXIT IF YOU USE CHROME AS YOU BROWSER.                  #
# WAIT FOR THE ANIMATION TO FINISH BEFORE CLOSING YOUR TAB                    #
###############################################################################


import numpy as np
from mayavi import mlab
import vpython as vp
import matplotlib.pyplot as plt
import datetime


################################################
#              INITIAL CONDITIONS              #
################################################

# Moments of inertia with respect to the principle axes of the body
lambda1, lambda2, lambda3 = 1, 2, 3


# Allow the user to easily choose from a set of
# initial angular velocities
print("Choose a set of initial angular velocities:")
print("")
print("a: omega1(0) = 1, omega2(t) = .1, omega3(0) = .01")
print("b: omega1(0) = .01, omega2(t) = .1, omega3(0) = 1")
print("c: omega1(0) = 10^-8, omega2(t) = 1, omega3(0) = 10^-3")
print("")
print("type 'a', 'b', or 'c' to select one of the options")
choice = input()


while choice != 'a' and choice != 'b' and choice != 'c':
    print("Invalid selection, please try again")
    print("type 'a', 'b', or 'c' to select one of the options")
    choice = input()

if choice == 'a':
    omega1_initial = .01
    omega2_initial = .1
    omega3_initial = 1
    L1_fig1 = 0
    L2_fig1 = 0
    L3_fig1 = lambda3

elif choice == 'b':
    omega1_initial = 1
    omega2_initial = .1
    omega3_initial = .01
    L1_fig1 = lambda1
    L2_fig1 = 0
    L3_fig1 = 0

elif choice == 'c':
    omega1_initial = 1e-8
    omega2_initial = 1
    omega3_initial = 1e-3
    L1_fig1 = 0
    L2_fig1 = lambda2
    L3_fig1 = 0

# Initial value of euler angle phi of the object in body frame
phi_initial = 0


################################################
#  SOLVING THE ODINARY DIFFERENTIAL EQUATIONS  #
################################################

computing_start = datetime.datetime.now()
print("Computing ODEs this may take a moment...")

# An array that holds the values of omega1(t), omega2(t), omega3(t) and phi(t)
values = np.array([omega1_initial, omega2_initial, omega3_initial,
                   phi_initial])


# Magnitude of the Angular Momentum
L_magnitude = np.sqrt((lambda1**2)*(omega1_initial**2) +
                      (lambda2**2)*(omega2_initial**2) +
                      (lambda3**2)*(omega3_initial**2))


# Number of iterations for the calculation of the ODEs.
iterations = 100000


# Function that contains the 4 ODEs. Holds Eq(1)
def ODEs(arr=values):
    '''
    ------------------------ODEs---------------------------
    Euler's set of coupled differential equations for
    rotational mechanics in 3 dimensions

    Euler's angle of phi

    Args:
    arr: pass the array "values"

    Returns:
    Solutions for domega1, domega2, domega3, dphi as an array.
    Each element in the array represents a solution to each
    respective ODEs for one time step
    '''

    omega1 = arr[0]
    omega2 = arr[1]
    omega3 = arr[2]
    domega1 = ((lambda2 - lambda3)*omega3*omega2)/(lambda1)
    domega2 = ((lambda3 - lambda1)*omega1*omega3)/(lambda2)
    domega3 = ((lambda1 - lambda2)*omega2*omega1)/(lambda3)
    dphi = (((omega1**2)*lambda1 +
            (omega2**2)*lambda2) / ((omega1**2)*lambda1**2 +
            (omega2**2)*lambda2**2)*L_magnitude)

    return np.array([domega1, domega2, domega3, dphi], float)


# Function that solves the ODEs. Solve Eq(1)
def Runge_Kutta(ODE=ODEs, arr=values, start=0, end=100, N=iterations):
    '''
    ---------------------Runge_Kutta------------------------
    Solves Euler's Equations of rotation and the Euler Angle phi
    using 4th order Runge Kutta. Runge Kutta is a technique
    that solves ODE and systems of ODEs numerically (note below for more info)

    Args:
    ODE: pass the function "Eulers_rotation_equations"
    arr: pass the array "values"
    start: Start of interval
    end: End of interval
    N: Number of steps

    Return:
    omega#_points - Each omega array holds all the omega# values for every
    moment in time
    tpoints - array of every time value that was calculated

    Note:
    Calculations are more accurate but slower
    as N and/or h is increased
    h: Step size

    An explaination of how the Runge-Kutta method works can be found in
    "Computational Physics" Chapter 8 Section 1.3 by Mark Newman (pg. 336)
    '''

    # Compute step size
    h = (end-start)/N

    # Create an array of evenly distributed time points
    # using the step size h, and the interval endpoints
    tpoints = np.arange(start, end, h)

    # Create lists that will store each respective omega(t) value
    omega1_points = np.array([])
    omega2_points = np.array([])
    omega3_points = np.array([])
    phi_points = np.array([])

    # Runge Kutta Method
    # As t increments by h (as defined by tpoints) we append
    # new omega values to the lists. Each omega appended is a numerical
    # solution of Euler's Equations
    for t in tpoints:
        omega1_points = np.append(omega1_points, arr[0])
        omega2_points = np.append(omega2_points, arr[1])
        omega3_points = np.append(omega3_points, arr[2])
        phi_points = np.append(phi_points, arr[3])
        k1 = h*ODE(arr)
        k2 = h*ODE(arr + .5*k1)
        k3 = h*ODE(arr + .5*k2)
        k4 = h*ODE(arr + k3)
        arr += (k1 + 2*k2 + 2*k3 + k4) / 6
    return omega1_points, omega2_points, omega3_points, tpoints, phi_points


# Get all the values of omega1, omega2, omega3, t, and phi
# Store solutions of Eq(1), Eq(12) and time values
omega1_points, omega2_points, omega3_points, tpoints, phi = Runge_Kutta()

print("Done!")
computing_end = datetime.datetime.now()
computing_duration = (computing_end - computing_start).total_seconds()
print(f"These ODEs took {computing_duration} seconds to calculate")


###############################################
#   ENERGY & ANGULAR MOMENTUM CONSERVATION    #
###############################################


# Interval of possible angles in spherical coordinates
u = np.linspace(0, 2*np.pi, 100)  # [0, 2pi]
v = np.linspace(0, np.pi, 100)  # [0, pi]


# Ellipsoid equation for angular momentum. Eq (5)
Lx_Ellipsoid = np.outer(np.cos(u), np.sin(v))
Ly_Ellipsoid = np.outer(np.sin(u), np.sin(v))
Lz_Ellipsoid = np.outer(np.ones_like(u), np.cos(v))


# Rotational Kinetic Energy. Eq (6)
K = (.5*(lambda1)*(omega1_initial**2) +
     .5*(lambda2)*(omega2_initial**2) +
     .5*(lambda3)*(omega3_initial**2))


# Radii coeffecients for the kinetic energy ellipsoid. Eq (7)
K_radii = (.5*((L_magnitude)**2)/(K*lambda1),
           .5*((L_magnitude)**2)/(K*lambda2),
           .5*((L_magnitude)**2)/(K*lambda3))
Kx, Ky, Kz = 1/np.sqrt(K_radii)


# Convert spherical values to cartesian
Kx_Ellipsoid = Kx * np.outer(np.cos(u), np.sin(v))
Ky_Ellipsoid = Ky * np.outer(np.sin(u), np.sin(v))
Kz_Ellipsoid = Kz * np.outer(np.ones_like(u), np.cos(v))


# Components of Angular Momentum (Vector L). Eq (2)
L1 = lambda1*omega1_points
L2 = lambda2*omega2_points
L3 = lambda3*omega3_points


# Components of the angular momentum (Unit Vector l_hat). Eq (4)
l1_hat = (L1)/(L_magnitude)
l2_hat = (L2)/(L_magnitude)
l3_hat = (L3)/(L_magnitude)


###############################################
#      CALCULATION OF THE ROTATION MATRIX     #
###############################################


# Euler angles of the rotation matrix. Eq (12)
theta = np.arccos(l3_hat)
psi = np.arctan2(l1_hat, l2_hat)
# phi was solved when we solved Euler's equations b/c it is dependent on omega


# Components of the unit vectors in the direction of principle axes. Eq (14)
Px = (np.cos(psi)*np.cos(phi)) - (np.cos(theta)*np.sin(phi)*np.sin(psi))
Py = (np.cos(psi)*np.sin(phi)) + (np.cos(theta)*np.cos(phi)*np.sin(psi))
Pz = np.sin(theta)*np.sin(psi)

Qx = -(np.sin(psi)*np.cos(phi)) - (np.cos(theta)*np.sin(phi)*np.cos(psi))
Qy = -(np.sin(psi)*np.sin(phi)) + (np.cos(theta)*np.cos(phi)*np.cos(psi))
Qz = np.sin(theta)*np.cos(psi)

Rx = np.sin(theta)*np.sin(phi)
Ry = -(np.sin(theta)*np.cos(phi))
Rz = np.cos(theta)


###############################################
#      PLOTS OF ELLIPSOIDS & l2 VS TIME       #
###############################################


# Use Mayavi to plot the ellipsoids in Fig 1
mlab.figure(bgcolor=(1, 1, 1))
mlab.points3d(L1_fig1/L_magnitude, L2_fig1/L_magnitude, L3_fig1/L_magnitude,
              color=(1, 0, 0), scale_factor=.1)
mlab.points3d(-L1_fig1/L_magnitude, -L2_fig1/L_magnitude, -L3_fig1/L_magnitude,
              color=(1, 0, 0), scale_factor=.1)
mlab.mesh(Kx_Ellipsoid, Ky_Ellipsoid, Kz_Ellipsoid,
          color=(1, .643, .282), transparent=True)
mlab.mesh(Lx_Ellipsoid, Ly_Ellipsoid, Lz_Ellipsoid,
          color=(0, .510, .753), transparent=True)
mlab.show()


# Use Mayavi to plot the ellipsoids in Figs 2, 3, 4
mlab.clf
mlab.figure(bgcolor=(1, 1, 1))
mlab.plot3d(l1_hat, l2_hat, l3_hat, color=(1, 0, 0))
mlab.plot3d(-l1_hat, -l2_hat, -l3_hat, color=(1, 0, 0))
mlab.mesh(Kx_Ellipsoid, Ky_Ellipsoid, Kz_Ellipsoid,
          color=(1, .643, .282), transparent=False)
mlab.mesh(Lx_Ellipsoid, Ly_Ellipsoid, Lz_Ellipsoid,
          color=(0, .510, .753), transparent=False)
mlab.show()


# Use Matplotlib to show relationship between l2 and time for Fig 8
plt.plot(tpoints, l2_hat, label='l2', color='green')
plt.title('l2 vs t')
plt.xlabel('time')
plt.ylabel('l2')
plt.legend()
plt.show()


###############################################
#           ANIMATIONS WITH VPYTHON           #
###############################################

# Vpython is used for Figs 5, 6 ,7


# Pause Button for the animation
running = True


# Function required for the pause button
def Run(b):
    global running
    running = not running
    if running:
        b.text = "Pause"
    else:
        b.text = "Run"


# Create a Vpython Canvas for the T_shaped_handle Animation
origin = vp.vector(0, 0, 0)
T_shaped_handle = vp.canvas(width=900, height=740, center=origin)
T_shaped_handle.align = 'right'
T_shaped_handle.forward = vp.vector(-1, -.03, -1)
T_shaped_handle.background = vp.color.white
button = vp.button(text="Pause", pos=T_shaped_handle.title_anchor, bind=Run)


# Create the T-shaped handle from the T_shaped_handle Effect
p_hat_pos = vp.cylinder(pos=origin,
                        axis=vp.vector(Px[0], Py[0], Pz[0]),
                        radius=.15, color=vp.color.gray(.65))
p_hat_neg = vp.cylinder(pos=origin,
                        axis=vp.vector(-Px[0], -Py[0], -Pz[0]),
                        radius=.15, color=vp.color.gray(.65))
q_hat_DE = vp.cylinder(pos=origin,
                       axis=vp.vector(Qx[0], Qy[0], Qz[0]),
                       radius=.1, color=vp.color.gray(.65))


# Create trails for the T-shaped handle
p_hat_pos_trail = vp.sphere(pos=vp.vector(Px[0], Py[0], Pz[0]),
                            radius=.001, color=vp.color.red, make_trail=True,
                            retain=25)
p_hat_neg_trail = vp.sphere(pos=vp.vector(-Px[0], -Py[0], -Pz[0]),
                            radius=.001, color=vp.color.red, make_trail=True,
                            retain=25)
q_hat_DE_trail = vp.sphere(pos=vp.vector(Qx[0], Qy[0], Qz[0]),
                           radius=.001, color=vp.color.green,  make_trail=True,
                           retain=100)


# Create a Vpython Canvas for the Principle Axes Animation
Principle_Axes = vp.canvas(width=900, height=740, center=origin)
Principle_Axes.align = 'left'
Principle_Axes.forward = vp.vector(-1, -0.3, -1)
Principle_Axes.background = vp.color.white


# Create a set of Axes
x_axis = vp.cylinder(pos=origin, axis=vp.vector(1, 0, 0), radius=.01,
                     color=vp.color.gray(.1), opacity=.75)
y_axis = vp.cylinder(pos=origin, axis=vp.vector(0, 1, 0), radius=.01,
                     color=vp.color.gray(.1), opacity=.75)
z_axis = vp.cylinder(pos=origin, axis=vp.vector(0, 0, 1), radius=.01,
                     color=vp.color.gray(.1), opacity=.75)


# Labels for each Axes
x_text = vp.text(text='X', pos=vp.vector(1.1, 0, 0), align='center',
                 height=0.05, color=vp.color.gray(.1), billboard=True,
                 emissive=True)
y_text = vp.text(text='Y', pos=vp.vector(0, 1.1, 0), align='center',
                 height=0.05, color=vp.color.gray(.1), billboard=True,
                 emissive=True)
z_text = vp.text(text='Z', pos=vp.vector(0, 0, 1.1), align='center',
                 height=0.05, color=vp.color.gray(.1), billboard=True,
                 emissive=True)


# Create the vectors of the principle axes that will rotate
p_hat = vp.cylinder(pos=origin,
                    axis=vp.vector(Px[0], Py[0], Pz[0]),
                    radius=.05, color=vp.color.red)
q_hat = vp.cylinder(pos=origin,
                    axis=vp.vector(Qx[0], Qy[0], Qz[0]),
                    radius=.05, color=vp.color.green)
r_hat = vp.cylinder(pos=origin,
                    axis=vp.vector(Rx[0], Ry[0], Rz[0]),
                    radius=.05, color=vp.color.blue)


# Create trails for the vectors of the principle axes
p_hat_trail = vp.sphere(pos=vp.vector(Px[0], Py[0], Pz[0]),
                        radius=.005, color=vp.color.red, make_trail=True,
                        retain=2500)
q_hat_trail = vp.sphere(pos=vp.vector(Qx[0], Qy[0], Qz[0]),
                        radius=.005, color=vp.color.green,  make_trail=True,
                        retain=100)
r_hat_trail = vp.sphere(pos=vp.vector(Rx[0], Ry[0], Rz[0]),
                        radius=.005, color=vp.color.blue,  make_trail=True,
                        retain=100)


# Run the Animations with Vpython using a loop
# if statement allows the pause button to work
vp.sleep(1)
i = 0
while i < iterations:
    if running is True:
        vp.rate(60)
        r1 = vp.vector(Px[i], Py[i], Pz[i])
        r2 = vp.vector(Qx[i], Qy[i], Qz[i])
        r3 = vp.vector(Rx[i], Ry[i], Rz[i])
        r1_neg = vp.vector(-Px[i], -Py[i], -Pz[i])

        # Updates the vectors
        p_hat_pos.axis = r1
        p_hat_neg.axis = r1_neg
        q_hat_DE.axis = r2
        p_hat.axis = r1
        q_hat.axis = r2
        r_hat.axis = r3

        # Updates the trails
        p_hat_pos_trail.pos = r1
        p_hat_neg_trail.pos = r1_neg
        q_hat_DE_trail.pos = r2
        p_hat_trail.pos = r1
        q_hat_trail.pos = r2
        r_hat_trail.pos = r3
    else:
        pass


print("")
print("End of Program.")
