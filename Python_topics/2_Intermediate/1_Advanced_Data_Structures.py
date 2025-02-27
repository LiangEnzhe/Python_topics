# ----------------------------------------------------------------------
# List Comprehensions and Generator Expressions
# ----------------------------------------------------------------------

# 1. List Comprehensions:
# A concise way to create lists by applying an operation to each item in a sequence.
# Syntax: [expression for item in iterable if condition]

# Example: Create a list of squares of even numbers
numbers = [1, 2, 3, 4, 5, 6]
squares_of_evens = [x**2 for x in numbers if x % 2 == 0]
print(squares_of_evens)  # Prints: [4, 16, 36]

# Example: Flatten a 2D list into a 1D list
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in matrix for item in sublist]
print(flattened)  # Prints: [1, 2, 3, 4, 5, 6]

# 2. Generator Expressions:
# Similar to list comprehensions but produce a generator object (lazy evaluation).
# Syntax: (expression for item in iterable if condition)

# Example: Generate squares of numbers (lazy evaluation)
squares_gen = (x**2 for x in range(5))
print(next(squares_gen))  # Prints: 0 (first value)
print(next(squares_gen))  # Prints: 1 (second value)

# Generators are memory-efficient compared to list comprehensions.

# ----------------------------------------------------------------------
# Advanced Dictionary Methods and Dictionary Comprehensions
# ----------------------------------------------------------------------

# 1. Advanced Dictionary Methods

# Example dictionary
person = {"name": "Alice", "age": 30}

# get(): Safely access a value for a key, with a default if the key doesn't exist.
print(person.get("name", "Unknown"))  # Prints: Alice
print(person.get("job", "Unemployed"))  # Prints: Unemployed (default value)

# update(): Merge another dictionary into the current dictionary.
new_info = {"age": 31, "job": "Engineer"}
person.update(new_info)  # Updates 'age' and adds 'job'
print(person)  # Prints: {'name': 'Alice', 'age': 31, 'job': 'Engineer'}

# Example: Access all keys, values, or items (key-value pairs)
print(person.keys())  # Prints: dict_keys(['name', 'age', 'job'])
print(person.values())  # Prints: dict_values(['Alice', 31, 'Engineer'])
print(person.items())  # Prints: dict_items([('name', 'Alice'), ('age', 31), ('job', 'Engineer')])

# 2. Dictionary Comprehensions:
# A concise way to create dictionaries.
# Syntax: {key_expression: value_expression for item in iterable if condition}

# Example: Create a dictionary of squares
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # Prints: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Example: Swap keys and values in a dictionary
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # Prints: {1: 'a', 2: 'b', 3: 'c'}

# ----------------------------------------------------------------------
# deque from the collections Module
# ----------------------------------------------------------------------
# A `deque` (double-ended queue) is a list-like data structure optimized for fast
# appends and pops from both ends.

from collections import deque

# 1. Create a deque
dq = deque([1, 2, 3])  # Create a deque with initial elements
print(dq)  # Prints: deque([1, 2, 3])

# 2. Append and appendleft
dq.append(4)  # Append to the right
dq.appendleft(0)  # Append to the left
print(dq)  # Prints: deque([0, 1, 2, 3, 4])

# 3. Pop and popleft
dq.pop()  # Remove and return the rightmost element
print(dq)  # Prints: deque([0, 1, 2, 3])
dq.popleft()  # Remove and return the leftmost element
print(dq)  # Prints: deque([1, 2, 3])

# 4. Rotate
# Rotate the deque elements by n steps.
dq.rotate(1)  # Rotate to the right by 1
print(dq)  # Prints: deque([3, 1, 2])
dq.rotate(-1)  # Rotate to the left by 1
print(dq)  # Prints: deque([1, 2, 3])

# 5. Extend and extendleft
dq.extend([4, 5])  # Add multiple elements to the right
print(dq)  # Prints: deque([1, 2, 3, 4, 5])
dq.extendleft([0, -1])  # Add multiple elements to the left (reversed order)
print(dq)  # Prints: deque([-1, 0, 1, 2, 3, 4, 5])
