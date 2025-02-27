# ----------------------------------------------------------------------
# Custom Exceptions
# ----------------------------------------------------------------------
# In Python, you can define custom exceptions by creating a new class that
# inherits from the built-in `Exception` class.

# Example: Defining a custom exception
class NegativeValueError(Exception):
    """Exception raised when a negative value is encountered."""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative values are not allowed: {value}")

# Example: Using the custom exception
def process_value(value):
    """Process the value, raising an error if it's negative."""
    if value < 0:
        raise NegativeValueError(value)  # Raise the custom exception
    return value * 2  # Example processing: doubling the value

# Handling the custom exception
try:
    print(process_value(-10))  # Pass a negative value to trigger the exception
except NegativeValueError as e:
    print(e)  # Prints: Negative values are not allowed: -10

# Example: Another custom exception with additional context
class InvalidInputError(Exception):
    """Exception raised for invalid inputs with extra details."""
    def __init__(self, input_value, message="Invalid input provided"):
        self.input_value = input_value
        self.message = message
        super().__init__(f"{message}: {input_value}")

# Example: Using the exception
try:
    user_input = "abc"  # Simulate invalid input
    if not user_input.isdigit():
        raise InvalidInputError(user_input, "Expected a numeric value")
except InvalidInputError as e:
    print(e)  # Prints: Expected a numeric value: abc

# ----------------------------------------------------------------------
# Best Practices in Exception Handling
# ----------------------------------------------------------------------

# 1. Catch Specific Exceptions
# Avoid catching generic `Exception` unless necessary. Be specific to improve debugging.
try:
    result = 10 / 0
except ZeroDivisionError:  # Catching specific exception
    print("Division by zero is not allowed.")
# Generic catch-all for unexpected errors (use with caution)
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# 2. Use `finally` for Cleanup
# Always release resources like files, database connections, or locks in the `finally` block.
try:
    file = open("example.txt", "r")  # Open a file for reading
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    if 'file' in locals() and not file.closed:
        file.close()  # Ensure the file is closed
    print("Cleanup complete.")

# 3. Avoid Silencing Exceptions
# Avoid empty `except` blocks that swallow errors without handling or logging them.
try:
    result = int("not a number")
except ValueError:
    print("Conversion failed. Please provide a valid integer.")
# Avoid this bad practice:
# except:
#     pass  # Silently ignores the error, making debugging harder.

# 4. Use Custom Exceptions for Clarity
# Use custom exceptions to handle domain-specific errors and improve code readability.
class InsufficientFundsError(Exception):
    """Exception raised for insufficient funds."""
    pass

def withdraw(balance, amount):
    """Withdraw an amount from the balance, raising an error if insufficient funds."""
    if amount > balance:
        raise InsufficientFundsError("Not enough funds available.")
    return balance - amount

try:
    print(withdraw(100, 150))  # Attempt to withdraw more than the balance
except InsufficientFundsError as e:
    print(e)  # Prints: Not enough funds available.

# 5. Log Exceptions
# Use logging instead of printing to track exceptions in production environments.
import logging

logging.basicConfig(level=logging.ERROR)  # Set up logging
try:
    value = int("abc")  # Trigger a ValueError
except ValueError as e:
    logging.error(f"Error occurred: {e}")

# 6. Use Assertions for Debugging
# Use `assert` to catch programming errors during development (not in production).
def divide(a, b):
    """Divide two numbers, ensuring the divisor is not zero."""
    assert b != 0, "The divisor must not be zero."  # Assert will raise AssertionError if false
    return a / b

try:
    print(divide(10, 0))  # This will trigger AssertionError
except AssertionError as e:
    print(e)  # Prints: The divisor must not be zero.

# 7. Rethrow Exceptions (When Necessary)
# Catch an exception to log or perform some action, then rethrow it if needed.
try:
    raise ValueError("Some error occurred")
except ValueError as e:
    print(f"Logging error: {e}")
    raise  # Rethrow the exception
