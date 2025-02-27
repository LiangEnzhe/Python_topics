# ----------------------------------------------------------------------
# 1. Try, Except, Finally
# ----------------------------------------------------------------------
# The try-except block is used to handle exceptions (errors) that occur during program execution.
# - 'try': Code that may raise an exception.
# - 'except': Code to execute if an exception occurs.
# - 'finally': Code that will execute no matter what (optional).

# Example 1: Basic try-except
try:
    # Code that may raise an exception
    num = int(input("Enter a number: "))  # This will raise ValueError for non-integer input
    print(f"You entered {num}")
except ValueError:  # Handle the ValueError exception
    print("That's not a valid number!")

# Example 2: Try-Except-Finally
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:  # Handle ZeroDivisionError
    print("Cannot divide by zero!")
finally:
    print("This code runs no matter what.")  # Always executes

# Example 3: Multiple except blocks
try:
    # Code that may raise exceptions
    x = int(input("Enter a number: "))  # May raise ValueError
    print(10 / x)  # May raise ZeroDivisionError
except ValueError:
    print("Invalid input! Please enter an integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# ----------------------------------------------------------------------
# 2. Raising Exceptions with raise
# ----------------------------------------------------------------------
# Use 'raise' to manually trigger an exception in your code.
# You can raise built-in exceptions or define custom exceptions.

# Example 1: Raising a built-in exception
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")  # Raise ValueError with a custom message
    print(f"Age is valid: {age}")

try:
    validate_age(-5)
except ValueError as e:
    print(e)  # Prints: Age cannot be negative!

# Example 2: Raising custom exceptions
# Define a custom exception by inheriting from the built-in Exception class
class CustomError(Exception):
    """Custom exception for demonstration."""
    pass

def demo_custom_exception(value):
    if value == "error":
        raise CustomError("Custom error triggered!")  # Raise the custom exception
    print(f"Value is: {value}")

try:
    demo_custom_exception("error")
except CustomError as e:
    print(e)  # Prints: Custom error triggered!
