import numpy as np


def Fourier(y, percentage=.15):
    """
    Fourier(y, percentage)

    Positional Arg: y
    takes an array and returns
    a fourier transformed function z

    Keyword Arg: percentage
    takes a float between 0 and 1 and
    applies it to array y. The difference is percentage
    of elements of array y that are converted to 0.
    By default the last 85% of array y is converted to 0s.
    """
    # use FFT to get array with .5N + 1 elements
    c = np.fft.rfft(y)

    # set abritary % of array to zero
    d = int(len(c)*(percentage))
    e = len(c) - d
    c = (c[:d])
    c = np.pad(c, (0, e), 'constant')

    # run irfft
    z = np.fft.irfft(c)
    return z
