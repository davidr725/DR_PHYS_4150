import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# Initial conditions
Radius = .1
theta_0 = (179 * (np.pi/180))
omega_0 = 0
x_initial = Radius * np.cos(theta_0)
y_initial = Radius * np.sin(theta_0)


# ODE function of Pendulum we want to solve
def f(r, t, arm_length=Radius, g=9.8):
    theta = r[0]
    omega = r[1]
    d_theta = omega
    d_omega = -(g/arm_length)*np.sin(theta)
    return np.array([d_theta, d_omega], float)


# Runge-Kutta Method to Solve ODE
def RungeKutta(ODE_function,
               theta_initial=theta_0, omega_initial=omega_0,
               a=0, b=10, N=1000):

    # Set/Reset arrays
    h = (b-a)/N  # Step Size
    tpoints = np.arange(a, b, h)
    theta_points = []
    omega_points = []
    r = np.array([theta_initial, omega_initial], float)

    # Loop to calculate the ODE
    for t in tpoints:
        theta_points.append(r[0])
        omega_points.append(r[1])
        k1 = h*ODE_function(r, t)
        k2 = h*ODE_function(r + .5*k1, t + .5*h)
        k3 = h*ODE_function(r + .5*k2, t + .5*h)
        k4 = h*ODE_function(r + k3, t+h)
        r += (k1 + 2*k2 + 2*k3 + k4) / 6

    return theta_points, omega_points, tpoints


# Returned Values from ODE Solver
theta_points, omega_points, tpoints = RungeKutta(f)


# Points for Graphs
x = Radius * np.cos(theta_points)
y = Radius * np.sin(theta_points)
theta_points = np.array(theta_points, float) * (180/np.pi)


# Slice the list of points, frames for the animation
# Running 1000 frames, lowering to 360 sliced

def List_Slice(z):
    z_start = z[:55:3]
    z_mid = z[55:75]
    z_end = z[75:126:3]
    z = []
    z = np.append(z, z_start)
    z = np.append(z, z_mid)
    z = np.append(z, z_end)
    z = np.append(z, np.flipud(z_end))
    z = np.append(z, np.flipud(z_mid))
    z = np.append(z, np.flipud(z_start))
    z = np.array(z, float)
    return z


x = List_Slice(x)
y = List_Slice(y)


# Matplotlib Plots
fig, ax = plt.subplots(2, 1, figsize=(6, 8))
ax[0].plot(tpoints, theta_points, color='tab:orange')
ax[0].set_title("Position")
ax[1].plot(tpoints, omega_points)
ax[1].set_title("Angular Velocity")
plt.show()


# Plotly Plot
fig = go.Figure(
    data=[go.Scatter(x=[0, y_initial], y=[0, -x_initial])],
    layout=go.Layout(
        xaxis=dict(range=[-.15, .15], autorange=False),
        yaxis=dict(range=[-.15, .15], autorange=False),
        title="Pendulum Simulation",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Start",
                          method="animate",
                          args=[None])])]),
    frames=[go.Frame(
        data=[go.Scatter(
            x=[0, y[k]],
            y=[0, -x[k]],
            mode="lines+markers",
            marker=dict(color="red", size=10))])
            for k in range(len(x))])
fig.show()
