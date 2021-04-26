import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# ODE function
def f(r, t, m, radius=.08, rho=1.22, drag_coeff=.47, g=9.8):
    vx = r[2]
    vy = r[3]
    dvx = -.5*(1/m)*np.pi*radius*rho*drag_coeff*np.sqrt(vx**2 + vy**2)*vx
    dvy = -.5*(1/m)*np.pi*radius*rho*drag_coeff*np.sqrt(vx**2 + vy**2)*vy - g
    return np.array([vx, vy, dvx, dvy], float)


# Trajectory Function
def trajectory(ODE_function, m, phi=30, x_initial=0, y_initial=0,
               V_initial=100, a=0, b=10, N=1000):
    # Step Size
    h = (b-a)/N

    # Set/Reset arrays
    xpoints = []
    ypoints = []
    tpoints = np.arange(a, b, h)

    # Problem initialization
    V_xi = np.cos(np.radians(phi))*V_initial  # x component of initial velocity
    V_yi = np.sin(np.radians(phi))*V_initial  # y component of initial velocity
    r = np.array([x_initial, y_initial, V_xi, V_yi], float)

    # Loop to calculate the ODE
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        k1 = h*ODE_function(r, t, m)
        k2 = h*ODE_function(r + .5*k1, t + .5*h, m)
        k3 = h*ODE_function(r + .5*k2, t + .5*h, m)
        k4 = h*ODE_function(r + k3, t+h, m)
        r += (k1 + 2*k2 + 2*k3 + k4) / 6
        if r[1] <= 0:
            tkept = tpoints[tpoints <= t]
            break
    return xpoints, ypoints, tkept


# Trajectories superposition & time values for varying masses
xpoints_1, ypoints_1, tkept_1 = trajectory(f, 2)
xpoints_2, ypoints_2, tkept_2 = trajectory(f, 4)
xpoints_3, ypoints_3, tkept_3 = trajectory(f, 8)


# Matplotlib Plots
plt.plot(xpoints_1, ypoints_1, label='Mass = 2 kg')
plt.plot(xpoints_2, ypoints_2, label='Mass = 4 kg')
plt.plot(xpoints_3, ypoints_3, label='Mass = 8 kg')
plt.title('Trajectory Plot in Matplotlib')
plt.legend()
plt.show()

# Plotly Plots
fig = go.Figure()

# Improve visability for graph
tkept_1 *= 10
tkept_2 *= 10
tkept_3 *= 10

fig.add_trace(go.Scatter(x=xpoints_1, y=ypoints_1, mode='markers',
              marker_size=tkept_1, name='Mass = 2 kg'))
fig.add_trace(go.Scatter(x=xpoints_2, y=ypoints_2, mode='markers',
              marker_size=tkept_2, name='Mass = 4 kg'))
fig.add_trace(go.Scatter(x=xpoints_3, y=ypoints_3, mode='markers',
              marker_size=tkept_3, name='Mass = 8 kg'))
fig.update_layout(title='Trajectory Plot in Plotly')
fig.show()
