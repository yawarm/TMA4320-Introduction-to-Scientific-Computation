import numpy as np

def f(x):
    """
    Function to integrate.

    Parameters:
        x (float or ndarray): Input value(s).

    Returns:
        float or ndarray: The value of x^2.
    """
    return x**2

def f_double_prime(x):
    """
    Second derivative of the function `f`.

    Parameters:
        x (float or ndarray): Input value(s).

    Returns:
        float or ndarray: The value of the second derivative, which is 2.
    """
    return 2 + 0*x

def step_calc(lower, upper, decimal_place):
    """
    Calculate the required number of steps to achieve a specified decimal precision.

    Parameters:
        lower (float): The lower bound of the integration interval.
        upper (float): The upper bound of the integration interval.
        decimal_place (int): Desired decimal precision.

    Returns:
        int: The calculated number of steps, rounded up.
    """
    x = np.linspace(lower, upper, 1000)
    max_second_derivative = max(abs(f_double_prime(x)))
    steps = np.sqrt((upper - lower)**3 * max_second_derivative / (12 * 10**(-decimal_place)))
    return int(np.ceil(steps))

def midpoint_error(lower, upper, steps):
    """
    Estimate the error for the Midpoint method.

    Parameters:
        lower (float): The lower bound of the integration interval.
        upper (float): The upper bound of the integration interval.
        steps (int): The number of steps used in the integration.

    Returns:
        float: The estimated error.
    """
    x = np.linspace(lower, upper, 1000)
    max_second_derivative = max(abs(f_double_prime(x)))
    h = (upper - lower) / steps
    error = (upper - lower) * h**2 / (24 * max_second_derivative)
    return error

def midpoint_method(lower, upper, steps):
    """
    Perform integration using the Midpoint method.

    Parameters:
        lower (float): The lower bound of the integration interval.
        upper (float): The upper bound of the integration interval.
        steps (int): The number of steps for the integration.

    Returns:
        tuple: The estimated integral and the associated error.
    """
    h = (upper - lower) / steps
    S = 0
    for i in range(steps):
        midpoint = lower + (i + 0.5) * h
        S += f(midpoint)
    integral = S * h
    error = midpoint_error(lower, upper, steps)
    return integral, error

# Run the code
if __name__ == "__main__":
    lower = 0
    upper = 1
    decimal_place = 5

    # Calculate the required steps for the desired precision
    steps = step_calc(lower, upper, decimal_place)
    print(f"To achieve precision to {decimal_place} decimal places, use more than {steps} steps.")

    # Perform the integration using the Midpoint method
    integral, error = midpoint_method(lower, upper, steps)
    print(f"The integral has value {integral:.10f} with an estimated error of {error:.10f}.")
