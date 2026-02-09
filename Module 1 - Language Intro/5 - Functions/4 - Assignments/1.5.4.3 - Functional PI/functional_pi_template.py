import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """
    a = 1
    b = 1 / (2 ** 0.5)
    t = 1/4
    p = 1

    pi_estimate = 100
    while abs(pi_estimate - math.pi) > target_error:
        y = a
        a_n = (a + b) / 2
        b_n = (a * b) ** (1/2)
        t_n = t - (p * ((y - a_n) ** 2))
        p_n = 2 * p

        pi_estimate = ((a_n + b_n) ** 2) / (4 * t_n)

        a = a_n
        b = b_n
        t = t_n
        p = p_n


    # change this so an actual value is returned
    return pi_estimate




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
