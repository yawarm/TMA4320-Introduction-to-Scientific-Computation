def point_generator(n):
    """
    Generate a list of points based on user input.

    Parameters:
        n (int): The number of points to generate.

    Returns:
        list: A list of tuples representing the points (x, y).
    """
    points = []
    for i in range(n):
        x = float(input(f"Enter the x-value for point {i + 1}: "))
        y = float(input(f"Enter the y-value for point {i + 1}: "))
        points.append((x, y))
    return points

def lagrange_interpolation(points):
    """
    Perform Lagrange interpolation and display the resulting polynomial as a string.

    Parameters:
        points (list): A list of tuples representing the points (x, y).

    Returns:
        None
    """
    n = len(points)
    coefficients = []  # Stores the coefficients for the polynomial

    # Calculate coefficients of the Lagrange polynomial
    for i in range(n):
        denominator = 1
        for j in range(n):
            if j != i:
                denominator *= (points[i][0] - points[j][0])
        coefficient = points[i][1] / denominator
        coefficients.append(coefficient)

    # Construct and display the polynomial
    print("The Lagrange interpolation polynomial is:")
    polynomial_terms = []

    for i in range(n):
        term = f"{coefficients[i]}"
        for j in range(n):
            if j != i:
                term += f"*(x - {points[j][0]})"
        polynomial_terms.append(term)

    # Combine all terms
    polynomial = " + ".join(polynomial_terms)
    print(f"{polynomial}")

# Example usage
num_points = 3  # Number of points to input
points = point_generator(num_points)
lagrange_interpolation(points)
