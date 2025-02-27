# ----------------------------------------------------------------------
# map(), filter(), and reduce()
# ----------------------------------------------------------------------

# 1. map(): Applies a function to each element in an iterable and returns a map object.
# Example: Square each number in a list
numbers = [1, 2, 3, 4, 5]

# Define a function
def square(x):
    return x**2

# Use map() to apply the function to each element
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Prints: [1, 4, 9, 16, 25]

# Use map() with a lambda function for brevity
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  # Prints: [1, 4, 9, 16, 25]

# ----------------------------------------------------------------------

# 2. filter(): Filters elements of an iterable based on a condition.
# Example: Filter out even numbers from a list
numbers = [1, 2, 3, 4, 5]

# Define a function to check for odd numbers
def is_odd(x):
    return x % 2 != 0

# Use filter() to apply the condition
odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))  # Prints: [1, 3, 5]

# Use filter() with a lambda function
odd_numbers = filter(lambda x: x % 2 != 0, numbers)
print(list(odd_numbers))  # Prints: [1, 3, 5]

# ----------------------------------------------------------------------

# 3. reduce(): Applies a function cumulatively to the items of an iterable, reducing it to a single value.
from functools import reduce

# Example: Compute the product of all numbers in a list
numbers = [1, 2, 3, 4]

# Define a function for multiplication
def multiply(x, y):
    return x * y

# Use reduce() to apply the function
product = reduce(multiply, numbers)
print(product)  # Prints: 24

# Use reduce() with a lambda function
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Prints: 24

# ----------------------------------------------------------------------
# The functools Module
# ----------------------------------------------------------------------
# The `functools` module provides tools for working with functions, including decorators and higher-order functions.

from functools import partial, lru_cache

# 1. partial(): Create a new function with some arguments fixed.
def power(base, exponent):
    return base ** exponent

# Create a new function that always raises numbers to the power of 2
square = partial(power, exponent=2)
print(square(4))  # Prints: 16

# 2. lru_cache(): Cache results of expensive function calls to improve performance.
@lru_cache(maxsize=128)  # Cache up to 128 results
def fibonacci(n):
    """Compute the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Prints: 55
# Subsequent calls to fibonacci(10) will be faster due to caching.

# ----------------------------------------------------------------------
# The itertools Module
# ----------------------------------------------------------------------
# The `itertools` module provides efficient tools for iterators.

import itertools

# 1. count(): Infinite iterator that generates consecutive numbers.
counter = itertools.count(start=10, step=2)  # Start at 10, increment by 2
print(next(counter))  # Prints: 10
print(next(counter))  # Prints: 12

# 2. cycle(): Infinite iterator that cycles through an iterable.
colors = itertools.cycle(["red", "blue", "green"])
print(next(colors))  # Prints: red
print(next(colors))  # Prints: blue

# 3. repeat(): Repeat a value a specified number of times.
repeated_values = itertools.repeat("Python", 3)
print(list(repeated_values))  # Prints: ['Python', 'Python', 'Python']

# 4. permutations(): Generate all possible orderings of elements.
letters = ["a", "b", "c"]
perms = itertools.permutations(letters)
print(list(perms))  # Prints: [('a', 'b', 'c'), ('a', 'c', 'b'), ...]

# 5. combinations(): Generate all possible combinations (no repeated orders).
combs = itertools.combinations(letters, 2)
print(list(combs))  # Prints: [('a', 'b'), ('a', 'c'), ('b', 'c')]

# 6. accumulate(): Cumulatively apply a function (default is addition).
numbers = [1, 2, 3, 4]
accumulated = itertools.accumulate(numbers)
print(list(accumulated))  # Prints: [1, 3, 6, 10] (cumulative sums)
