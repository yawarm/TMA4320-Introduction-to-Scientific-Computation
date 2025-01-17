import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = x + cos(x) - sin(x)
# This is the function whose fixed point we are trying to find using Fixed Point Iteration
# Input: x (float or ndarray) - The input value for the function
# Output: (float or ndarray) - The result of f(x) = x + cos(x) - sin(x)
def f(x):
    return x + np.cos(x) - np.sin(x)

# Define the linear function g(x) = x
# This function is used for plotting purposes to compare with f(x)
# Input: x (float or ndarray) - The input value for the function
# Output: (float or ndarray) - The result of g(x) = x
def g(x):
    return x

# Arrays to store points for plotting (used in Fixed Point Iteration visualization)
x_points = np.ndarray(3)
y_points = np.ndarray(3)

# Fixed Point Iteration (FPI) method to find a fixed point of a function f(x)
# The algorithm starts with an initial guess and iteratively applies f(x) to approach a fixed point
# Input: 
#   initial_guess (float) - The initial guess for the fixed point
#   error_threshold (float) - The stopping criterion based on the difference between successive estimates
#   plot (bool) - Whether to plot the iterations (default is False)
# Output: 
#   current_x (float) - The final fixed point estimate
#   iterations (int) - The number of iterations taken to reach the fixed point
#   error_threshold (float) - The threshold value used for stopping criteria
def fixed_point_iteration(initial_guess, error_threshold, plot=False):
    iterations = 1  # Counter for the number of iterations
    previous_x = initial_guess  # Initialize the first guess
    
    # If plotting is enabled, store the initial guess for visualization
    if plot:
        x_points[0], y_points[0] = previous_x, previous_x
    
    # Perform the first iteration using f(x)
    current_x = f(previous_x)
    if plot:
        x_points[1], y_points[1] = previous_x, current_x
        x_points[2], y_points[2] = current_x, current_x
        plt.plot(x_points, y_points, '-k')  # Plot the first iteration line

    # Continue iterating until the error between successive guesses is less than the threshold
    while np.abs(current_x - previous_x) > error_threshold:
        previous_x = current_x  # Update the previous guess with the current value
        if plot:
            x_points[0], y_points[0] = previous_x, previous_x  # Store the current x for plotting
        current_x = f(previous_x)  # Apply f(x) to get the next estimate
        if plot:
            x_points[1], y_points[1] = previous_x, current_x  # Store the new points for plotting
            x_points[2], y_points[2] = current_x, current_x
            plt.plot(x_points, y_points, '-k')  # Plot the new iteration line
        iterations += 1  # Increment iteration counter
    
    return current_x, iterations, error_threshold  # Return the final estimate, iterations, and threshold used

# Run the Fixed Point Iteration (FPI) with an initial guess of 0 and error threshold of 1e-10
# The result will contain the fixed point, the number of iterations, and the error threshold used
result = fixed_point_iteration(0, 1e-10, plot=True)

# Output the results of the fixed point iteration
print(f"Fixed Point with error threshold {result[2]} is: {result[0]}")
print(f"FPI ran {result[1]} iterations")

# Plot the functions f(x) and g(x) for comparison
x_vals = np.linspace(-2, 2, 100)  # Generate values for x between -2 and 2 for plotting
plt.plot(x_vals, g(x_vals), label='g(x) = x')  # Plot g(x) = x
plt.plot(x_vals, f(x_vals), label='f(x) = x + cos(x) - sin(x)')  # Plot f(x)
plt.grid()  # Enable grid on the plot
plt.legend()  # Show legend to label the curves
plt.show()  # Display the plot
