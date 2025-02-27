# ----------------------------------------------------------------------
# Lists: Indexing, Slicing, and Methods
# ----------------------------------------------------------------------
# Lists are mutable sequences used to store an ordered collection of items.

# Example of a list
fruits = ["apple", "banana", "cherry"]

# 1. Indexing
# Access elements using their position (index starts from 0).
print(fruits[0])  # Prints: apple
print(fruits[-1])  # Prints: cherry (negative indexing starts from the end)

# 2. Slicing
# Access a subset of the list using slicing.
# Syntax: list[start:end:step]
print(fruits[0:2])  # Prints: ['apple', 'banana'] (from index 0 to 1, excluding 2)
print(fruits[::2])  # Prints: ['apple', 'cherry'] (every second element)

# 3. Methods
# Lists have various methods to manipulate their contents.

# append(): Adds an item to the end of the list.
fruits.append("date")
print(fruits)  # Prints: ['apple', 'banana', 'cherry', 'date']

# pop(): Removes and returns the last item (or the item at a specified index).
removed_item = fruits.pop()
print(removed_item)  # Prints: date
print(fruits)  # Prints: ['apple', 'banana', 'cherry']

# sort(): Sorts the list in ascending order (modifies the original list).
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Prints: [1, 2, 3, 4]

# Note: Use sorted() for a new sorted list without modifying the original.

# ----------------------------------------------------------------------
# Tuples and Their Immutability
# ----------------------------------------------------------------------
# Tuples are immutable sequences, meaning their elements cannot be changed.

# Example of a tuple
coordinates = (10, 20, 30)

# Access tuple elements with indexing and slicing (like lists).
print(coordinates[1])  # Prints: 20
print(coordinates[:2])  # Prints: (10, 20)

# Attempting to modify a tuple raises an error.
# coordinates[0] = 15  # TypeError: 'tuple' object does not support item assignment

# Tuples are useful for representing fixed collections of data.

# Unpacking tuples:
x, y, z = coordinates
print(x, y, z)  # Prints: 10 20 30

# ----------------------------------------------------------------------
# Sets and Set Operations
# ----------------------------------------------------------------------
# Sets are unordered collections of unique items.
# Useful for eliminating duplicates or performing mathematical set operations.

# Example of a set
numbers = {1, 2, 3, 4, 4}  # Duplicate 4 is automatically removed
print(numbers)  # Prints: {1, 2, 3, 4}

# Add an element to a set
numbers.add(5)
print(numbers)  # Prints: {1, 2, 3, 4, 5}

# Remove an element from a set
numbers.remove(3)
print(numbers)  # Prints: {1, 2, 4, 5}

# Set operations:
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union: Combine elements from both sets.
print(set_a | set_b)  # Prints: {1, 2, 3, 4, 5}

# Intersection: Elements common to both sets.
print(set_a & set_b)  # Prints: {3}

# Difference: Elements in set_a but not in set_b.
print(set_a - set_b)  # Prints: {1, 2}

# Symmetric Difference: Elements in either set, but not both.
print(set_a ^ set_b)  # Prints: {1, 2, 4, 5}

# ----------------------------------------------------------------------
# Dictionaries: Key-Value Pairs and Methods
# ----------------------------------------------------------------------
# Dictionaries store data as key-value pairs.

# Example of a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Access values using keys.
print(person["name"])  # Prints: Alice

# Add or update a key-value pair.
person["job"] = "Engineer"  # Add a new key-value pair
person["age"] = 26  # Update the value for an existing key
print(person)  # Prints: {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}

# Remove a key-value pair using pop().
removed_value = person.pop("city")
print(removed_value)  # Prints: New York
print(person)  # Prints: {'name': 'Alice', 'age': 26, 'job': 'Engineer'}

# Dictionary Methods:
# keys(): Returns a view of all keys.
print(person.keys())  # Prints: dict_keys(['name', 'age', 'job'])

# values(): Returns a view of all values.
print(person.values())  # Prints: dict_values(['Alice', 26, 'Engineer'])

# items(): Returns a view of all key-value pairs as tuples.
print(person.items())  # Prints: dict_items([('name', 'Alice'), ('age', 26), ('job', 'Engineer')])

# Get a value with a default if the key does not exist using get().
print(person.get("city", "Not Found"))  # Prints: Not Found

# Check if a key exists.
print("age" in person)  # Prints: True

# ----------------------------------------------------------------------
# enumerate()
# ----------------------------------------------------------------------

# The enumerate() function adds a counter to an iterable (like a list, tuple, or string)
# and returns it as an enumerate object, which can be converted into a list of tuples.

fruits = ["apple", "banana", "cherry"]
enumerated_fruits = enumerate(fruits)  # Creates an enumerate object

# Convert to a list to see the output
print(list(enumerated_fruits))  
# Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    # Output:
    # 0: apple
    # 1: banana
    # 2: cherry

file_lines = ["First line", "Second line", "Third line"]
for line_number, line in enumerate(file_lines, start=1):
    print(f"Line {line_number}: {line}")
    # Output:
    # Line 1: First line
    # Line 2: Second line
    # Line 3: Third line