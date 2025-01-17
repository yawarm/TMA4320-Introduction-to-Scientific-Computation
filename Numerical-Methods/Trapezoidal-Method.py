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

def f_double_prime(x):
    """
    Second derivative of the function `f`.

    Parameters:
        x (float or ndarray): Input value(s).

    Returns:
        float or ndarray: The value of the second derivative, 2 * cos(x) - x * sin(x).
    """
    return 2 * np.cos(x) - x * np.sin(x)

def step_calc(lower, upper, decimal_place):
    """
    Calculate the required number of steps to achieve a specified decimal precision using the trapezoidal rule.

    Parameters:
        lower (float): The lower bound of the integration interval.
        upper (float): The upper bound of the integration interval.
        decimal_place (int): Desired decimal precision.

    Returns:
        int: The calculated number of steps, rounded up.
    """
    x = np.linspace(lower, upper, 1000)
    max_second_derivative = max(abs(f_double_prime(x)))
    steps = np.sqrt((upper - lower)**3 * max_second_derivative / (6 * 10**(-decimal_place)))
    return int(np.ceil(steps))

def trapezoidal_error(lower, upper, steps):
    """
    Estimate the error for the trapezoidal rule.

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
    error = ((upper - lower) * h**2) / 12 * max_second_derivative
    return error

def trapezoidal_rule(lower, upper, steps):
    """
    Perform integration using the trapezoidal rule.

    Parameters:
        lower (float): The lower bound of the integration interval.
        upper (float): The upper bound of the integration interval.
        steps (int): The number of steps for the integration.

    Returns:
        tuple: The estimated integral and the associated error.
    """
    h = (upper - lower) / steps
    S = 0.5 * (f(lower) + f(upper))

    # Sum the contributions of intermediate points
    for i in range(1, steps):
        S += f(lower + i * h)

    integral = h * S
    error = trapezoidal_error(lower, upper, steps)
    return integral, error

# Run the code
if __name__ == "__main__":
    lower = 0
    upper = 1
    decimal_place = 5

    # Calculate the required steps for the desired precision
    steps = step_calc(lower, upper, decimal_place)
    print(f"To achieve precision to {decimal_place} decimal places, use more than {steps} steps.")

    # Perform the integration using the trapezoidal rule
    integral, error = trapezoidal_rule(lower, upper, steps)
    print(f"The integral has value {integral:.10f} with an estimated error of {error:.10f}.")
