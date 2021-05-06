import numpy as np
import scipy.constants as cons
import scipy.fftpack as fft
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Computational Functions
def psi0(x):
    '''
    Returns the first value of psi at time = 0
    for all given values of x
    '''
    x0 = L/2
    sigma = 1e-10
    kappa = 5e10
    numerator = (x-x0)**2
    denominator = 2*(sigma**2)
    psi_0 = np.exp(-(numerator/denominator))*np.exp(1j*kappa*x)
    return psi_0


def Z(t):
    '''
    This returns the inverse discrete sine transform
    at a specific time giving a value of the wave
    function.
    '''
    cos_term = t*(((np.pi**2)*hbar*(k**2)) / (2*m*(L**2)))
    sin_term = t*(((np.pi**2)*hbar*(k**2)) / (2*m*(L**2)))

    alpha_term = np.cos(cos_term) * coefficents_real
    eta_term = np.sin(sin_term) * coefficents_imag

    z = alpha_term - eta_term
    inverse_z = fft.idst(z) / N
    return inverse_z


# Animation functions
def init():
    line.set_data(xpoints, psi0(xpoints))
    return line,


def animate(i):
    x = xpoints
    y = Z(time[i])
    line.set_data(x, y)
    return line,


'''
Important Note!

N and t_end must be of equal array length
because the animation function is dependent on
the product of both the N & t_end arrays
with one another.

If they are of unequal length the animation
will end abruptly when it gets to the element
in the array where the lengths no longer match.
'''

# Initial conditions
m = cons.electron_mass
L = 1e-8
hbar = cons.hbar
h = 1e-18
N = 25000
a = L/N

# Positon & Time points
time = (h)*np.arange(N)
t_end = N
k = np.linspace(0, N, num=N+1, endpoint=False)
k = np.delete(k, 0)
xpoints = a*np.linspace(0, N, num=N+1, endpoint=False)
xpoints = np.delete(xpoints, 0)  # delete the boundary condition

# Perform the DST on the psi to retrieve the coeffecients
psi = psi0(xpoints)
coefficents = fft.dst(psi)

# Split the coefficents into their real and imaginary components
coefficents_real = np.real(coefficents)
coefficents_imag = np.imag(coefficents)

# Animation
fig = plt.figure()
axis = plt.axes(xlim=(-1e-9, 11e-9), ylim=(-2, 2))
axis.set_xlabel('x')
axis.set_ylabel('$\psi(x)$')
axis.set_title('Spectral Wave Function')
line, = axis.plot([], [], lw=.5)

ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=t_end, interval=10, blit=True,
    save_count=50)

plt.show()
