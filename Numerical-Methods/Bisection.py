import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import math

# ---------------------------------
def f(x):
    """
    Function for which we are finding the roots.

    Parameters:
        x (float or ndarray): Input value(s).

    Returns:
        float or ndarray: The result of cos(x) - sin(x^2).
    """
    return np.cos(x) - np.sin(x**2)

# ---------------------------------
def bisection(a, b, tol):
    """
    Perform the Bisection method to find a root of the function `f`.

    Parameters:
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        tol (float): The tolerance for stopping the iterations.

    Returns:
        tuple: (number of iterations, estimated root).
    """
    xl = a
    xr = b
    i = 1

    while np.abs(xl - xr) >= tol:
        c = (xl + xr) / 2.0  # Midpoint
        prod = f(xl) * f(c)

        if prod > 0:
            xl = c  # Root is in the right subinterval
        elif prod < 0:
            xr = c  # Root is in the left subinterval
        else:
            break  # Exact root found

        i += 1

    return i, c

# ---------------------------------
def num_iterations(a, b, decimal_precision):
    """
    Calculate the theoretical number of iterations needed for the Bisection method
    to achieve a given decimal precision.

    Parameters:
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        decimal_precision (int): Desired decimal precision.

    Returns:
        tuple: (theoretical number of iterations, decimal precision).
    """
    n = (decimal_precision * (b - a)) / np.log10(2)
    return n, decimal_precision

# ---------------------------------
# Analyze the number of iterations needed for a given decimal precision
print("Analysis:")
iterations = num_iterations(0, 1, 10)
print(f"Number of iterations to get within {iterations[1]} decimal places: {math.ceil(iterations[0])}")
print(f"The Bisection method will use {math.ceil(iterations[0]) + 2} iterations to get the result\n")

# Run the Bisection method
answer = bisection(0, 1, 0.5e-10)
print(f"Bisection Method Gives Root At x = {answer[1]}")
print(f"Iterations: {answer[0]}")

# Plot the function
x = np.linspace(-1, 1, 100)
plt.plot(x, f(x), label='f(x) = cos(x) - sin(x^2)')
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Add x-axis
plt.grid()
plt.legend()
plt.title("Bisection Method: Root Finding")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

# ---------------------------------
# Shortcut using fsolve
# Uncomment the following lines to use `fsolve` for root finding:
# shortcut = fsolve(f, [-1.5, 1.5])
# print(f"Fsolve gives root(s) at x = {shortcut}")
# ---------------------------------
