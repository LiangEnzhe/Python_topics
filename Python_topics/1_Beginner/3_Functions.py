# ----------------------------------------------------------------------
# 1. Defining and Calling Functions
# ----------------------------------------------------------------------
# Functions are blocks of reusable code that perform specific tasks.
# They help organize code and avoid repetition.

# Syntax:
# def function_name(parameters):
#     """Optional docstring describing the function."""
#     # Code block
#     return value  # Optional, used to return a result

# Example: Function without parameters
def greet():
    """Prints a greeting message."""
    print("Hello, World!")

# Calling the function
greet()  # Prints: Hello, World!

# Example: Function with parameters
def greet_person(name):
    """Greets a person by name."""
    print(f"Hello, {name}!")

greet_person("Alice")  # Prints: Hello, Alice!

# ----------------------------------------------------------------------
# 2. Function Arguments and Return Values
# ----------------------------------------------------------------------
# Functions can accept arguments (input values) and return values (output).

# Example: Function with arguments and return value
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add(3, 5)  # Call the function and store the result
print(result)  # Prints: 8

# Multiple return values:
# A function can return multiple values as a tuple.
def math_operations(x, y):
    """Performs multiple math operations and returns results."""
    sum_result = x + y
    diff_result = x - y
    prod_result = x * y
    return sum_result, diff_result, prod_result

results = math_operations(10, 5)
print(results)  # Prints: (15, 5, 50)

# ----------------------------------------------------------------------
# 3. Default Arguments and Keyword Arguments
# ----------------------------------------------------------------------
# Default arguments allow functions to have default values for parameters.
# If no value is provided, the default value is used.

# Example: Function with default arguments
def greet_with_default(name="Guest"):
    """Greets a person with a default name if none is provided."""
    print(f"Hello, {name}!")

greet_with_default()  # Prints: Hello, Guest!
greet_with_default("Bob")  # Prints: Hello, Bob!

# Keyword arguments allow specifying arguments by their parameter name.
# This improves readability and allows arguments to be passed in any order.

# Example: Keyword arguments
def order_food(main_course, drink, dessert):
    """Prints an ordered meal."""
    print(f"Main course: {main_course}, Drink: {drink}, Dessert: {dessert}")

# Call using positional arguments
order_food("Pizza", "Coke", "Ice Cream")
# Call using keyword arguments (order can vary)
order_food(drink="Water", dessert="Cake", main_course="Pasta")

# Mixing positional and keyword arguments:
# Positional arguments must come before keyword arguments.
# Correct:
order_food("Burger", drink="Juice", dessert="Pie")
# Incorrect:
# order_food(drink="Juice", "Burger", dessert="Pie")  # SyntaxError

# ----------------------------------------------------------------------
# 4. Lambda Functions (Anonymous Functions)
# ----------------------------------------------------------------------
# Lambda functions are small, anonymous functions defined with the 'lambda' keyword.
# They can have multiple arguments but only one expression (which is returned).

# Syntax:
# lambda arguments: expression

# Example: Lambda function to add two numbers
add_lambda = lambda a, b: a + b
print(add_lambda(3, 5))  # Prints: 8

# Example: Lambda with no arguments
hello_lambda = lambda: "Hello, Lambda!"
print(hello_lambda())  # Prints: Hello, Lambda!

# Lambdas are often used with higher-order functions like map(), filter(), and sorted().

# Example: Using lambda with map() to double numbers in a list
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Prints: [2, 4, 6, 8]

# Example: Using lambda with filter() to filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Prints: [2, 4]
