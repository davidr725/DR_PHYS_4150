import numpy as np
import matplotlib.pyplot as plt
import FFT_Function as FFT


def squarewave(n):
    """
    squarewave(n)
    takes an argument n, n must be an array,
    and returns a square wave function with amplitude 1
    """
    y = np.arange(0, 1000, 1)
    for i in range(len(n)):
        if n[i] < .50000:
            y[i] = 0
        if n[i] >= .50000:
            y[i] = 1
    return y


def sawtooth(n):
    """
    sawtooth(n)
    takes an argument n
    and returns a sawtooth wave function with amplitude 1
    """
    y = n
    return y


def modulatedwave(n):
    """
    modulatedwave(n)
    takes an argument n, n must be an array,
    and returns a modulated sine wave with amplitude 1
    """
    N = len(n)
    y = np.arange(0, 1000, 1)/1000
    for i in range(N):
        y[i] = np.sin((np.pi*i)/N)*np.sin((20*np.pi*i)/N)
    return y


# x values
x = np.linspace(0, 1, 1000)

# f(x) values
y_squarewave = squarewave(x)
y_sawtooth = sawtooth(x)
y_modulatedwave = modulatedwave(x)

# fourier transformed values
z_squarewave = FFT.Fourier(y_squarewave)
z_sawtooth = FFT.Fourier(y_sawtooth)
z_modulatedwave = FFT.Fourier(y_modulatedwave)

# Plot the original functions vs ffts
fig, ax = plt.subplots(3, 2)
fig.tight_layout(h_pad=3)

# Square Wave vs FFT Square Wave
ax[0, 0].plot(x, y_squarewave)
ax[0, 0].set_title("Square")
ax[0, 1].plot(x, z_squarewave, color='tab:orange')
ax[0, 1].set_title("FFT Square")

# Sawtooth Wave vs FFT Sawtooth Wave
ax[1, 0].plot(x, y_sawtooth)
ax[1, 0].set_title("Sawtooth")
ax[1, 1].plot(x, z_sawtooth, color='tab:orange')
ax[1, 1].set_title("FFT Sawtooth")

# Modulated Sin Wave vs FFT Modulated Sin Wave
ax[2, 0].plot(x, y_modulatedwave)
ax[2, 0].set_title("Modulated Sine Wave")
ax[2, 1].plot(x, z_modulatedwave, color='tab:orange')
ax[2, 1].set_title("FFT Modulated Sine Wave")

# Format plots
plt.show()

# test for doc strings
# print(squarewave.__doc__)
# print(sawtooth.__doc__)
# print(modulatedwave.__doc__)
# print(FFT.Fourier.__doc__)
