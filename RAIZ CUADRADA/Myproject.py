import math

def calculate_square_root(number):
    """
    Calculates the square root of a given number.

    Args:
    - number (float): The number for which the square root will be calculated.

    Returns:
    - float: The value of the square root of the given number.
    
    Raises:
    - ValueError: If the input number is negative.
    """
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    
    return math.sqrt(number)

# Example of usage:
try:
    num = float(input("Enter a number to calculate its square root: "))
    result = calculate_square_root(num)
    print(f"The square root of {num} is: {result}")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Unexpected error: {e}")
