import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure(figsize=(25, 25))
ax = plt.axes(xlim=(-10, 110), ylim=(-10, 110))
scatter, = ax.plot(0, 0, color='r')
bounds = plt.Rectangle((0, 0), 100, 100, color='0.8')
ax.add_patch(bounds)
plt.title('Brownian Motion')
drunk_x = [50]
drunk_y = [50]


def update(i):
    """
    updated frame function for FuncAnimation Method in MatPlotlib
    requires no arguments from the user, argument i is passed from
    the FuncAnimation Method. It keeps track of the frame.
    """
    i += 1

    np.random.seed()
    z = np.random.randint(0, 4, dtype=int)

    # Move Right
    if z == 0:
        if drunk_x[-1] == 100:
            drunk_x.append(drunk_x[-1]-1)
            drunk_y.append(drunk_y[-1])
        else:
            drunk_x.append(drunk_x[-1]+1)
            drunk_y.append(drunk_y[-1])

    # Move Up
    if z == 1:
        if drunk_y[-1] == 100:
            drunk_y.append(drunk_y[-1]-1)
            drunk_x.append(drunk_x[-1])
        else:
            drunk_y.append(drunk_y[-1]+1)
            drunk_x.append(drunk_x[-1])

    # Move Left
    if z == 2:
        if drunk_x[-1] == 0:
            drunk_x.append(drunk_x[-1]+1)
            drunk_y.append(drunk_y[-1])
        else:
            drunk_x.append(drunk_x[-1]-1)
            drunk_y.append(drunk_y[-1])

    # Move Down
    if z == 3:
        if drunk_y[-1] == 0:
            drunk_y.append(drunk_y[-1]+1)
            drunk_x.append(drunk_x[-1])
        else:
            drunk_y.append(drunk_y[-1]-1)
            drunk_x.append(drunk_x[-1])

    # Create a list and save the previous 10 positions
    x = drunk_x[-1::-1]
    y = drunk_y[-1::-1]

    if len(x) >= 10:
        x = x[11:1:-1]
        x.append(drunk_x[-1])
        y = y[11:1:-1]
        y.append(drunk_y[-1])

    # Comments for troubleshooting
    # print('x' + str(x))
    # print('y' + str(y))

    scatter.set_xdata(x)
    scatter.set_ydata(y)
    return scatter,


ani = animation.FuncAnimation(fig, update,
                              frames=100, interval=1)
plt.show()
