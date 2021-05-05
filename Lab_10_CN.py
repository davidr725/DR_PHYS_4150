import numpy as np
import scipy.constants as cons
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def psi0(x):
    x0 = L/2
    sigma = 1e-10
    kappa = 5e10
    numerator = (x-x0)**2
    denominator = 2*(sigma**2)
    psi_0 = np.exp(-(numerator/denominator))*np.exp(1j*kappa*x)
    return psi_0


def tridiag_matrix(A, a1, a2):
    for i in range(N):
        A[i,i] = a1
        if i == 0:
            A[i, i+1] = a2
        elif i == N-1:
            A[i, i-1] = a2
        else:
            A[i, i+1] = a2
            A[i, i-1] = a2
    return A


# Initial conditions
m = cons.electron_mass
L = 1e-8
hbar = cons.hbar
h = 1e-18
N = 250
a = L/N
t = 0
t_end = 100000

# Xpoints
xpoints = a*np.linspace(0, N, num=N+1, endpoint=False)
xpoints = np.delete(xpoints, 0)  # delete the boundary condition

# Matrix elements
a1 = 1 + h*((1j*hbar)/(2*m*(a**2)))
a2 = -h*((1j*hbar)/(4*m*(a**2)))
b1 = 1 - h*((1j*hbar)/(2*m*(a**2)))
b2 = h*((1j*hbar)/(4*m*(a**2)))

# Create Tridiagonal Matrices A & B
MatrixA = np.zeros([N, N], dtype=complex)
MatrixA = tridiag_matrix(MatrixA, a1, a2)

MatrixB = np.zeros([N, N], dtype=complex)
MatrixB = tridiag_matrix(MatrixB, b1, b2)

# Animation
psi = []
psi.append(psi0(xpoints)) 
fig = plt.figure()
axis = plt.axes(xlim=(-1e-9, 11e-9), ylim=(-1, 1))
axis.set_xlabel('x')
axis.set_ylabel('$\psi(x)$')
axis.set_title('Crank Nicolson Wave Function')
line, = axis.plot([], [], lw = .5)


def init():
    line.set_data(xpoints, psi0(xpoints))
    return line,


def animate(i):
    v = np.dot(MatrixB, psi[i])
    psi.append(np.linalg.solve(MatrixA, v))
    x = xpoints
    y = psi[i]
    i += 2500
    line.set_data(x, y)

    return line,


ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=t_end, interval=0, blit=True,
    save_count=50)

plt.show()