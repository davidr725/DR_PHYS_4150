import numpy as np
import matplotlib.pyplot as plt


def RAD(element_1, element_2, element_3, element_4,
        list_1, list_2, list_3, list_4,
        tau_1, tau_2, tau_3,
        route_1, route_2,
        time_step=1, total_time=20000):

    """
    TBD
    """

    # Calculate the probabilities of decay based on tau
    decay_probability_1 = 1 - 2**(-time_step/(tau_1*60))
    decay_probability_2 = 1 - 2**(-time_step/(tau_2*60))
    decay_probability_3 = 1 - 2**(-time_step/(tau_3*60))

    # x values for graph
    tpoints = np.arange(0, total_time, time_step)

    # Main loop
    for i in tpoints:
        list_1.append(element_1)
        list_2.append(element_2)
        list_3.append(element_3)
        list_4.append(element_4)

    # Decay for first Element
        for i in range(element_1):
            if np.random.random() < decay_probability_1:
                if np.random.random() < route_1:
                    element_1 -= 1
                    element_3 += 1
                else:
                    element_1 -= 1
                    element_2 += 1

    # Decay for Second Element
        for j in range(element_2):
            if np.random.random() < decay_probability_2:
                element_2 -= 1
                element_3 += 1

    # Decay for Third Element
        for k in range(element_3):
            if np.random.random() < decay_probability_3:
                element_3 -= 1
                element_4 += 1

    return tpoints, list_1, list_2, list_3, list_4


# Element, Tau, & List 1
Bi213, Bi213_tau = 10000, 46
Bi213_list = []

# Element, Tau, & List 2
Ti209, Ti209_tau = 0, 2.2
Ti209_list = []

# Element, Tau, & List 3
Pb209, Pb209_tau = 0, 3.3
Pb209_list = []

# Element & List 4
Bi209 = 0
Bi209_list = []


x, a, b, c, d = RAD(Bi213, Ti209, Pb209, Bi209,
                    Bi213_list, Ti209_list, Pb209_list, Bi209_list,
                    Bi213_tau, Ti209_tau, Pb209_tau,
                    .9791, .0209)

# Format issue with Flake8
Bi213_list = a
Ti209_list = b
Pb209_list = c
Bi209_list = d

# Plot the decays
plt.plot(x, Bi213_list, label='Bi 213')
plt.plot(x, Ti209_list, label='Ti 209')
plt.plot(x, Pb209_list, label='Pb 209')
plt.plot(x, Bi209_list, label='Bi 209')
plt.title('Radioactive Decay Chain')
plt.xlabel('Time in seconds')
plt.ylabel('Number of atoms')
plt.legend()
plt.show()
