import numpy as np
import matplotlib.pyplot as plt

def Fourier(percentage):
    #A) plot dow data
    N = np.loadtxt('dow.txt')
    x = np.arange(0,len(N))

    #B) use FFT to get array with .5N + 1 elements
    c = np.fft.rfft(N)

    #C)set 90% of array to zero
    d = int(len(c)*(percentage))
    e = len(c) - d
    c = (c[:d])
    c = np.pad(c, (0,e), 'constant')

    #D)run irfft
    z = np.fft.irfft(c)

    plt.plot(x,N)
    plt.plot(x,z)
    plt.show()

#E)run program repeatedly with different percentages
Fourier(.05)


