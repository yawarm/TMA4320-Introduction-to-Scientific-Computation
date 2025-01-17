import numpy as np

def f(x):
    """
    Function to integrate.

    Parameters:
        x (float or ndarray): Input value(s).

    Returns:
        float or ndarray: The value of x * sin(x).
    """
    return x * np.sin(x)

def f_fourth_prime(x):
    """
    Fourth derivative of the function `f`.

    Parameters:
        x (float or ndarray): Input value(s).

    Returns:
        float or ndarray: The value of the fourth derivative, -3 * sin(x) - x * cos(x).
    """
    return -3 * np.sin(x) - x * np.cos(x)

def simpsons_method(lower, upper, steps):
    """
    Perform integration using Simpson's method over a fixed number of steps.

    Parameters:
        lower (float): The lower bound of the integration interval.
        upper (float): The upper bound of the integration interval.
        steps (int): The number of steps for the integration.

    Returns:
        float: The estimated integral.
    """
    h = (upper - lower) / steps
    integral_sum = (1 / 3) * (f(lower) + f(upper))

    # Simpson's rule for intermediate points
    for i in range(1, steps):
        if i % 2 == 0:
            integral_sum += (2 / 3) * f(lower + i * h)
        else:
            integral_sum += (4 / 3) * f(lower + i * h)

    return h * integral_sum

def adaptive_quadrature_simpson(lower, upper, tolerance):
    """
    Perform adaptive quadrature using Simpson's method.

    Parameters:
        lower (float): The lower bound of the integration interval.
        upper (float): The upper bound of the integration interval.
        tolerance (float): The desired accuracy for the integral approximation.

    Returns:
        tuple: The estimated integral and the number of iterations performed.
    """
    stack = [(lower, upper)]  # Stack to store subintervals
    total_integral = 0
    iteration = 0

    while stack:
        # Pop the current subinterval
        aa, bb = stack.pop()

        # Compute the integral over the subinterval and its midpoint
        integral_full = simpsons_method(aa, bb, 4)
        mid = (aa + bb) / 2
        integral_left = simpsons_method(aa, mid, 4)
        integral_right = simpsons_method(mid, bb, 4)

        # Increment iteration counter
        iteration += 1

        # Check for convergence in this subinterval
        if abs(integral_left + integral_right - integral_full) < 15 * tolerance * (bb - aa):
            total_integral += integral_left + integral_right
        else:
            # Subdivide the interval and push back onto the stack
            stack.append((mid, bb))
            stack.append((aa, mid))

        # Prevent infinite loop
        if iteration > 10000:
            print("Warning: Exceeded maximum iterations, stopping.")
            break

    return total_integral, iteration

# Run the code
if __name__ == "__main__":
    lower = 0
    upper = 1
    tolerance = 1e-6

    integral, iterations = adaptive_quadrature_simpson(lower, upper, tolerance)
    print(f"The integral has value: {integral:.10f} after {iterations} iterations.")
