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
        float or ndarray: The value of the fourth derivative, -3*sin(x) - x*cos(x).
    """
    return -3 * np.sin(x) - x * np.cos(x)

def step_calc(lower, upper, decimal_place):
    """
    Calculate the required number of steps to achieve a specified decimal precision using Simpson's method.

    Parameters:
        lower (float): The lower bound of the integration interval.
        upper (float): The upper bound of the integration interval.
        decimal_place (int): Desired decimal precision.

    Returns:
        int: The calculated number of steps, rounded up.
    """
    x = np.linspace(lower, upper, 1000)
    max_fourth_derivative = max(abs(f_fourth_prime(x)))
    steps = np.sqrt(np.sqrt((upper - lower)**5 * max_fourth_derivative / (90 * 10**(-decimal_place))))
    return int(np.ceil(steps))

def simpson_error(lower, upper, steps):
    """
    Estimate the error for Simpson's method.

    Parameters:
        lower (float): The lower bound of the integration interval.
        upper (float): The upper bound of the integration interval.
        steps (int): The number of steps used in the integration.

    Returns:
        float: The estimated error.
    """
    x = np.linspace(lower, upper, 1000)
    max_fourth_derivative = max(abs(f_fourth_prime(x)))
    h = (upper - lower) / steps
    error = ((upper - lower) * h**4) / (180 * max_fourth_derivative)
    return error

def simpsons_method(lower, upper, steps):
    """
    Perform integration using Simpson's method.

    Parameters:
        lower (float): The lower bound of the integration interval.
        upper (float): The upper bound of the integration interval.
        steps (int): The number of steps for the integration.

    Returns:
        tuple: The estimated integral and the associated error.
    """
    h = (upper - lower) / steps
    S = (1/3) * (f(lower) + f(upper))

    # Apply Simpson's rule
    for i in range(1, steps):
        if i % 2 == 0:
            S += (2/3) * f(lower + i * h)
        else:
            S += (4/3) * f(lower + i * h)

    integral = h * S
    error = simpson_error(lower, upper, steps)
    return integral, error

# Run the code
if __name__ == "__main__":
    lower = 0
    upper = 1
    decimal_place = 5

    # Calculate the required steps for the desired precision
    steps = step_calc(lower, upper, decimal_place)
    print(f"To achieve precision to {decimal_place} decimal places, use more than {steps} steps.")

    # Perform the integration using Simpson's method
    integral, error = simpsons_method(lower, upper, steps)
    print(f"The integral has value {integral:.10f} with an estimated error of {error:.10f}.")
