import autograd as ad
from autograd import grad, jacobian
import autograd.numpy as npp
import numpy as np

# --------------------------
# Example usage for testing (commented out):
# def example_function(x):
#     return x[0]**2 + x[1]**3

# z = np.array([5, 3], dtype="float")
# print(z)

# print(example_function(z))

# jacobian_func = jacobian(example_function)
# print(jacobian_func(z))

# --------------------------
# Define the functions and their Jacobians:

func1 = lambda x: x[0] - 2 * x[1] + 3 * x[2] - 7
jac_1 = jacobian(func1)

func2 = lambda x: 2 * x[0] + x[1] + x[2] - 4
jac_2 = jacobian(func2)

func3 = lambda x: -3 * x[0] + 2 * x[1] - 2 * x[2] + 10
jac_3 = jacobian(func3)

# ----------------------------
def multivariate_newton(eq_num, var_num, max_iterations):
    """
    Solve a system of nonlinear equations using the Newton-Raphson method.

    Parameters:
        eq_num (int): Number of equations in the system.
        var_num (int): Number of variables in the system.
        max_iterations (int): Maximum number of iterations to perform.

    Returns:
        tuple: A tuple containing the solution (numpy array) and the number of iterations performed.
    """
    if eq_num != var_num:
        print("Cannot solve systems where the number of equations and variables differ.")
        return None

    # Initialize variables
    iteration = 0
    initial_guesses = []

    # Collect initial guesses from the user
    for _ in range(var_num):
        guess = float(input("Enter your initial guess as a decimal: "))
        initial_guesses.append(guess)

    # Convert guesses to a numpy array
    guess = np.array(initial_guesses, dtype="float").reshape(var_num, 1)

    # Iterate until the solution converges or max iterations are reached
    while iteration < max_iterations:
        # Evaluate the functions at the current guess
        func_eval = np.array([
            func1(guess),
            func2(guess),
            func3(guess)
        ]).reshape(eq_num, 1)

        # Flatten guess for Jacobian calculation
        flat_guess = guess.flatten()

        # Compute the Jacobian matrix
        jacobian_matrix = np.array([
            jac_1(flat_guess),
            jac_2(flat_guess),
            jac_3(flat_guess)
        ]).reshape(var_num, eq_num)

        # Update guess using Newton-Raphson formula
        new_guess = guess - np.linalg.inv(jacobian_matrix) @ func_eval

        # Update guess and iteration counter
        guess = new_guess
        iteration += 1

    return new_guess, iteration

# Solve the system of equations
result = multivariate_newton(3, 3, 100)

if result is not None:
    print(f"\nSolution to the system of equations: {result[0].flatten()}")
    print(f"Iterations: {result[1]}")
