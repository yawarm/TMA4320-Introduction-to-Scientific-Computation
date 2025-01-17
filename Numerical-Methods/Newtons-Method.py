import numpy as np

def f(x):
    """
    Function for which we are finding the root.

    Parameters:
        x (float): Input value.

    Returns:
        float: The value of x^2 - 4.
    """
    return x**2 - 4

def f_prime(x):
    """
    Derivative of the function `f`.

    Parameters:
        x (float): Input value.

    Returns:
        float: The derivative, 2x.
    """
    return 2 * x

def newton_method(guess, max_iterations, tolerance, min_div=1e-20):
    """
    Perform the Newton-Raphson method to find a root of the function `f`.

    Parameters:
        guess (float): Initial guess for the root.
        max_iterations (int): Maximum number of iterations allowed.
        tolerance (float): Desired tolerance for the root approximation.
        min_div (float): Minimum denominator value to avoid division by very small numbers (default is 1e-20).

    Returns:
        tuple: A tuple containing the root (float) and the number of iterations (int).
        If the denominator becomes too small, returns (0, -1).
    """
    for i in range(max_iterations):
        fprime = f_prime(guess)

        # Check for small denominator to avoid numerical instability
        if abs(fprime) < min_div:
            print("Denominator too small: root may have high multiplicity.")
            return 0, -1

        # Newton-Raphson formula
        new_guess = guess - f(guess) / fprime

        # Compute the approximate error
        approx_error = abs(new_guess - guess)

        # Update the guess
        guess = new_guess

        # Check if tolerance is met
        if approx_error <= tolerance:
            print("Tolerance reached.")
            return new_guess, i + 1

    # If maximum iterations are reached, return the last guess
    print("Maximum iterations reached.")
    return guess, max_iterations

# Example usage
if __name__ == "__main__":
    initial_guess = 0
    max_iterations = 20
    tolerance = 1e-5

    result = newton_method(initial_guess, max_iterations, tolerance)
    print(f"The root is found to be: {result[0]:.6f}")
    print(f"Iterations: {result[1]}")
