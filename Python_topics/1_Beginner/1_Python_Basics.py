# ----------------------------------------------------------------------
# 1. Python Syntax
# ----------------------------------------------------------------------
# Python's syntax is the set of rules that define the structure of valid Python code.
# Syntax refers to the way in which statements and expressions are structured.

# Indentation (Spacing)
# Python uses indentation (spaces or tabs) to define blocks of code.
# For example, all code inside a function must be indented.

def greet(name):  # Function definition with a colon
    # Indented block (this is the body of the function)
    print(f"Hello, {name}!")  # Indentation shows this is inside the function

greet("Alice")  # Function call

# Note: Always use consistent indentation. Mixing tabs and spaces can cause errors.

# ----------------------------------------------------------------------
# 2. Python Keywords
# ----------------------------------------------------------------------
# Keywords are reserved words in Python that have a special meaning.
# They are used to define the structure of the Python program.
# These cannot be used as identifiers (like variable names).

# Example of some Python keywords
import keyword  # Importing the 'keyword' module to get all reserved keywords

print(keyword.kwlist)  # Display all keywords in Python

# Some common Python keywords:
# - def: Used to define a function
# - if, elif, else: Conditional statements
# - while, for: Looping statements
# - import: Used to import modules
# - class: Used to define a class
# - try, except: Error handling
# - return: Return value from a function

# ----------------------------------------------------------------------
# 3. Python Structure
# ----------------------------------------------------------------------
# Classes and Objects (OOP)
# Python supports Object-Oriented Programming (OOP) where you define classes 
# and create objects (instances) of those classes.

class Person:  # Define a class using the 'class' keyword
    def __init__(self, name, age):  # Constructor, initializes the object
        self.name = name  # Instance variable
        self.age = age    # Instance variable
    
    def introduce(self):  # Method of the class
        return f"Hello, I am {self.name} and I am {self.age} years old."

person1 = Person("Alice", 30)  # Create an object of the class Person
print(person1.introduce())  # Call method 'introduce'

# ----------------------------------------------------------------------
# 4. Common Python Structures Recap
# ----------------------------------------------------------------------

# Data Types:
# - Numbers: Integers (int), Floating-point numbers (float)
# - Sequences: Lists, Tuples, Strings
# - Sets: Unordered collection of unique items
# - Dictionaries: Key-value pairs (hash maps)

# Example of data types
a = 5  # Integer
b = 3.14  # Float
c = "Hello"  # String
d = [1, 2, 3]  # List
e = (1, 2, 3)  # Tuple
f = {1, 2, 3}  # Set
g = {'a': 1, 'b': 2}  # Dictionary

# ----------------------------------------------------------------------
# Data Types in Python
# ----------------------------------------------------------------------
# Python provides various built-in data types to store and manipulate data.
# Here, we focus on Strings, Integers, Floats, and Booleans.

# ----------------------------------------------------------------------
# 1. Strings
# ----------------------------------------------------------------------
# Strings are sequences of characters enclosed in single (' ') or double (" ") quotes.

# 1.1 String Operations
# Strings support many operations like concatenation, repetition, and slicing.
# Concatenation: Combining two strings using the '+' operator.
full_greeting = greeting + " My name is " + name

# Repetition: Repeat a string using the '*' operator.
repeated = name * 3
print(repeated)  # Prints: AliceAliceAlice

# Slicing: Access a part of the string using indices.
# Syntax: string[start:end:step]
substring = greeting[0:5]  # Extracts 'Hello'
print(substring)

# Strings are immutable (cannot be changed after creation), but new strings can be created.
# Use len() to get the length of the string.
length = len(greeting)
print(f"The length of the greeting is {length}")  # Prints: The length of the greeting is 13

# ----------------------------------------------------------------------
# 2. Integers
# ----------------------------------------------------------------------
# Integers (int) are whole numbers, positive or negative, without decimals.

# Integers support arithmetic operations like addition, subtraction, multiplication, etc.
a = 10
b = 3
print(a + b)  # Addition: Prints 13
print(a - b)  # Subtraction: Prints 7
print(a * b)  # Multiplication: Prints 30
print(a // b)  # Floor division: Prints 3 (integer result of division)
print(a % b)  # Modulus: Prints 1 (remainder)
print(a ** b)  # Exponentiation: Prints 1000 (10 to the power of 3)

# Integers can be of any size in Python (limited by memory).

# ----------------------------------------------------------------------
# 3. Floats
# ----------------------------------------------------------------------
# Floats (float) are numbers with decimals, used for representing real numbers.

# Floats support arithmetic operations similar to integers.
c = 5.0
d = 2.0
print(c + d)  # Addition: Prints 7.0
print(c - d)  # Subtraction: Prints 3.0
print(c * d)  # Multiplication: Prints 10.0
print(c / d)  # Division: Prints 2.5

# Floats can be rounded using the round() function.
rounded_pi = round(pi, 2)  # Rounds pi to 2 decimal places
print(f"Rounded value of pi: {rounded_pi}")  # Prints: Rounded value of pi: 3.14

# ----------------------------------------------------------------------
# 4. Booleans
# ----------------------------------------------------------------------
# Booleans (bool) represent two values: True and False.

# Example of booleans
is_python_fun = True
is_math_hard = False

# Booleans are often used in conditional statements.
if is_python_fun:
    print("Python is fun!")  # Prints: Python is fun!

# Boolean operations
# and, or, not are logical operators used with booleans.
print(True and False)  # Prints: False (both must be True)
print(True or False)  # Prints: True (one must be True)
print(not True)  # Prints: False (negation)

# Comparison operations return booleans.
x = 10
y = 20
print(x < y)  # Prints: True
print(x == y)  # Prints: False
print(x != y)  # Prints: True

# ----------------------------------------------------------------------
# Type Checking and Conversion
# ----------------------------------------------------------------------
# Use the type() function to check the type of a variable.
print(type(greeting))  # Prints: <class 'str'>
print(type(age))  # Prints: <class 'int'>
print(type(pi))  # Prints: <class 'float'>
print(type(is_python_fun))  # Prints: <class 'bool'>

# Convert between data types using str(), int(), float(), and bool().
num_str = "123"
converted_num = int(num_str)  # Convert string to integer
print(type(converted_num))  # Prints: <class 'int'>

float_to_int = int(3.99)  # Converts float to int (truncates decimal part)
print(float_to_int)  # Prints: 3

int_to_float = float(7)  # Converts integer to float
print(int_to_float)  # Prints: 7.0

# ----------------------------------------------------------------------
# Variables and Constants
# ----------------------------------------------------------------------
# Variables are containers for storing data. They can hold different types of values 
# and their values can change during the program's execution.

# Naming rules for variables:
# - Must start with a letter or underscore (_), not a number.
# - Can contain letters, numbers, and underscores.
# - Are case-sensitive (age and Age are different).

# Bad examples (will cause errors):
# 1user = "Invalid"  # Cannot start with a number
# user-name = "Invalid"  # Cannot contain hyphens

# Constants:
# Constants are variables whose values should not change during program execution.
# By convention, constants are written in ALL_CAPS.

# Example of constants
GRAVITY = 9.81  # Earth's gravity in m/s²
SPEED_OF_LIGHT = 299792458  # Speed of light in m/s

# Note: Python does not enforce immutability for constants; this is a convention.

# ----------------------------------------------------------------------
# Comments and Documentation
# ----------------------------------------------------------------------
# Comments are used to explain the code and make it more readable.
# Python ignores comments during execution.

# 1. Single-line comments:
# Single-line comments start with a hash (#).
# Example:
x = 10  # This is a single-line comment explaining the variable.

# 2. Multi-line comments:
# Multi-line comments (or docstrings) are enclosed in triple quotes (''' or """).
# They are often used to describe functions, classes, or modules.

"""
This is a multi-line comment.
It is often used to document the purpose of a script or a function.
"""

# Example of a docstring in a function
def add_numbers(a, b):
    """
    This function adds two numbers and returns the result.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of the two numbers.
    """
    return a + b

# Using comments effectively:
# - Explain the purpose of variables or complex logic.
# - Avoid redundant comments that simply describe the syntax.

# ----------------------------------------------------------------------
# Input/Output Functions
# ----------------------------------------------------------------------

# Input and Output functions allow interaction between the user and the program.

# 1. Output with print():
# The print() function is used to display information on the screen.

print("Hello, World!")  # Prints: Hello, World!

# Print variables or combine text and variables.
name = "Alice"
print("My name is", name)  # Prints: My name is Alice
print(f"My name is {name}")  # f-strings for formatted output: Prints: My name is Alice

# 2. Input with input():
# The input() function allows the user to provide data during program execution.

# Example of input():
user_name = input("Enter your name: ")  # Prompts the user to enter their name
print(f"Hello, {user_name}!")  # Prints a greeting with the entered name

# By default, input() returns data as a string.
# If you need a specific type (e.g., integer or float), convert it.
age = int(input("Enter your age: "))  # Converts the input to an integer
print(f"You are {age} years old.")  # Prints the entered age

# Note: Always validate input to ensure the program behaves as expected.
# Example: Check if the input is a number using try/except blocks to handle errors.
