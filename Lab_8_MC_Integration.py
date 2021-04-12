import numpy as np
import matplotlib.pyplot as plt


# Part A: prove the denonminator for p(x) is 2
def w(x):
    return (x**-.5)


sample_points_1 = 10000000
random_values_1 = np.random.random(sample_points_1)
I_denom_p = 1/(sample_points_1) * np.sum(w(random_values_1))
I_denom_p = round(I_denom_p, 2)
print('p(x) is: 1/(' + str(I_denom_p) + '*sqrt(x))')


# Part B: Evaluate the integral
def f(x):
    return (x**-.5)/(1+np.exp(x))


def p(x):
    return 1/(2*np.sqrt(x))


def g(x):
    return 1/(1+np.exp(x))


# Solving using f(x) and p(x)
sample_points_2 = 10000000
random_values_2 = np.random.random(sample_points_2)
integral = np.sum(f(random_values_2))/np.sum(p(random_values_2))
print('I is: ' + str(integral) + ' using f(x)/p(x)')


# Solving using g(x)
integral_2 = 1/sample_points_2 * I_denom_p * np.sum(g(random_values_2**2))
print('I is: ' + str(integral_2) + ' using g(x)')


plt.title('Probability Density Histogram')
plt.hist(random_values_2**2)
plt.show()
