import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from numpy.lib.shape_base import _replace_zero_by_x_arrays


# Initial conditions
I1 = 3
I2 = 1
I3 = 2
omega1_initial = 1e-8
omega2_initial = 1e-3
omega3_initial = 1
a = 0
b = 240
N = 50000
h = (b-a)/N

# ODE function
def Euler_EQs(r, t):
    omega1 = r[0]
    omega2 = r[1]
    omega3 = r[2]
    d_omega1 = ((I2 - I3)*omega2*omega3)/(I1)
    d_omega2 = ((I3 - I1)*omega1*omega3)/(I2)
    d_omega3 = ((I1 - I2)*omega1*omega2)/(I3)
    return np.array([d_omega1, d_omega2, d_omega3])


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


# Plot of each angular velocity in their respective axis
omega1_arr, omega2_arr, omega3_arr, time_arr = Euler_Solver(Euler_EQs)
plt.plot(time_arr, omega2_arr, label='omega 2')
plt.plot(time_arr, omega3_arr, label='omega 3')
plt.plot(time_arr, omega1_arr, label='omega 1')
plt.legend()
plt.show()

x_axis = np.linspace(-1, 1, N)
y_axis = np.linspace(-1, 1, N)
z_axis = np.linspace(-1, 1, N)
blank_axis = np.zeros(N)

# Plot of path of the omega vector
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax1.plot(xs=x_axis, ys=blank_axis, zs=blank_axis, color='blue')
ax1.plot(xs=blank_axis, ys=y_axis, zs=blank_axis, color='blue')
ax1.plot(xs=blank_axis, ys=blank_axis, zs=x_axis, color='blue')
ax1.plot(xs=omega1_arr, ys=omega2_arr, zs=omega3_arr, color='red')


ax1.set_xlim(-1, 1)
ax1.set_ylim(-1, 1)
ax1.set_zlim(-1, 1)
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.show()
