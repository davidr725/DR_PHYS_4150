import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as constants


def Lab_6(potential=20,w = 1e-9,err=0):
    #turn runtime warnings for divide by zero on or off
    if err == 0:
        np.seterr(divide='ignore')
    else:
        pass

    #given values
    mass=constants.electron_mass
    hbar = constants.hbar #J
    EV = constants.electron_volt #C
    constant_term = EV*(((w**2)*mass) / (2*hbar**2)) #EV

    #X values
    energy = np.linspace(0,potential,100)

    #given functions
    def y(energy):
        return np.tan(np.sqrt(constant_term*energy))

    def y_even(energy):
        return np.sqrt((potential-energy) / energy)

    def y_odd(energy):
        return -np.sqrt((energy) / (potential-energy))

    #Y values
    y1 = y(energy)
    y2 = y_even(energy)
    y3 = y_odd(energy)


    #plot the values
    plt.plot(energy,y1, label = 'general')
    plt.plot(energy,y2, label = 'even only')
    plt.plot(energy,y3, label = 'odd only')
    plt.legend()
    plt.show()


    #to make use of the bisection method we substract f(x)-g(x) to create a new curve h(x)
    #the roots of h(x) are where f(x) = g(x) for those particular values of x
    def even(energy):
        return (y(energy) - y_even(energy))

    def odd(energy):
        return y(energy) - y_odd(energy)


    #bisection method
    def bisection(x1,x2,f,err):
        midpoint = .5*(x1 + x2)
        while abs(x1 - x2) > err:
            if f(midpoint) == 0:
                return abs(x1 - x2)
            elif f(midpoint)*f(x1) > 0:
                x1 = midpoint
            else:
                x2 = midpoint
            midpoint = .5*(x1 + x2)
        return midpoint


    #odd energy values
    e1 = bisection(.2,.5,odd,1e-5)
    e3 = bisection(1,1.5,odd,1e-5)
    e5 = bisection(4.8,5.3,odd,1e-5)


    #even energy values
    e0 = bisection(2.5,3,even,1e-5)
    e2 = bisection(3,3.5,even,1e-5)
    e4 = bisection(7.5,8,even,1e-5)


    #print statements
    print("The first 3 odd energy values: ")
    print("e1: " + str(e1))
    print("e3: " + str(e3))
    print("e5: " + str(e5))
    print('')
    print("The first 3 even energy values: ")
    print("e0: " + str(e0))
    print("e2: " + str(e2))
    print("e4: " + str(e4))

Lab_6(w = 1e-9,err=0,potential=20)
