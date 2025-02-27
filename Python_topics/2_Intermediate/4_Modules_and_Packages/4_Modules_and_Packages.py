# ----------------------------------------------------------------------
# Modules and Packages in Python
# ----------------------------------------------------------------------
# A **module** is a single Python file containing reusable functions, classes, or variables.
# A **package** is a directory containing one or more modules, often organized into a folder
# with a special `__init__.py` file (used to define it as a package).

# ----------------------------------------------------------------------
# 1. Creating and Using Modules
# ----------------------------------------------------------------------

# Example: Creating a module (Save this as `math_utils.py` in the same directory as your main script)
# math_utils.py
"""
This module provides basic math utilities.
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

PI = 3.14159  # A constant in the module

# To use this module, import it in your main script.

# main_script.py
    import math_utils  # Import the math_utils module

    # Use functions and variables from the module
    result = math_utils.add(10, 5)
    print(f"10 + 5 = {result}")  # Prints: 10 + 5 = 15
    print(f"The value of PI is {math_utils.PI}")  # Prints: The value of PI is 3.14159

# ----------------------------------------------------------------------
# 2. Import Statement Variations
# ----------------------------------------------------------------------

# a. Importing specific items from a module
from math_utils import add, PI

# Use the imported items directly
result = add(3, 7)
print(f"3 + 7 = {result}")  # Prints: 3 + 7 = 10
print(f"PI = {PI}")  # Prints: PI = 3.14159

# b. Using an alias for a module
import math_utils as mu  # Alias the module as "mu"

result = mu.subtract(10, 5)
print(f"10 - 5 = {result}")  # Prints: 10 - 5 = 5

# c. Importing all items from a module (not recommended for large modules)
from math_utils import *

# Use all imported items without prefixing the module name
result = subtract(9, 4)  # Directly accessible
print(f"9 - 4 = {result}")  # Prints: 9 - 4 = 5

# d. Importing built-in or external modules
import math  # Built-in Python module
print(math.sqrt(16))  # Prints: 4.0

# ----------------------------------------------------------------------
# 3. Understanding Python Package Structure
# ----------------------------------------------------------------------
# A **package** is a directory that contains multiple modules and a special file `__init__.py`.
# The `__init__.py` file makes the directory a Python package.

# Example of a package structure:
# my_package/
# ├── __init__.py  # Defines the package and optional initialization code
# ├── math_utils.py
# └── string_utils.py

# Example: Contents of `__init__.py` (inside `my_package`)
"""
This is the __init__.py file for my_package.
You can use this to initialize the package or define what to import by default.
"""
__all__ = ["math_utils", "string_utils"]  # Explicitly define the modules to expose

# Importing from a package
from my_package import math_utils  # Import the math_utils module from the package

# Example of using the imported module
result = math_utils.add(4, 6)
print(f"4 + 6 = {result}")  # Prints: 4 + 6 = 10

# Importing everything defined in __all__ (from the package)
from my_package import *  # Imports math_utils and string_utils as defined in __init__.py

# ----------------------------------------------------------------------
# 4. Organizing Packages and Modules
# ----------------------------------------------------------------------
# Best Practices:
# - Organize related functionality into separate modules (files).
# - Group related modules into a package (folder).
# - Use descriptive names for modules and packages.
# - Document your modules and packages with docstrings.

# Example: A project structure
# my_project/
# ├── my_package/
# │   ├── __init__.py
# │   ├── math_utils.py
# │   └── string_utils.py
# ├── main_script.py
# └── README.md
