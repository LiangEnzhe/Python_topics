# ----------------------------------------------------------------------
# Optimizations and Profiling in Python
# ----------------------------------------------------------------------
# Profiling and optimization are critical for improving the performance of Python programs.
# This involves understanding bottlenecks, reducing memory usage, and improving runtime efficiency.

# ----------------------------------------------------------------------
# 1. Memory Optimization
# ----------------------------------------------------------------------

import sys
import gc

# a. Using `sys` to Measure Object Memory Size
# The `sys.getsizeof()` function returns the memory size of an object in bytes.

# Example: Measuring memory usage of different data structures
x = 10  # Integer
print(f"Memory used by integer: {sys.getsizeof(x)} bytes")  # Prints: Memory used by integer: 28 bytes

y = [1, 2, 3, 4, 5]  # List
print(f"Memory used by list: {sys.getsizeof(y)} bytes")  # Prints: Memory used by list: 96 bytes (size varies by implementation)

z = {"key": "value"}  # Dictionary
print(f"Memory used by dictionary: {sys.getsizeof(z)} bytes")  # Prints: Memory used by dictionary: 232 bytes

# b. Garbage Collection with `gc`
# Python's garbage collector (`gc`) automatically frees memory used by unreferenced objects.
# You can manually interact with the garbage collector.

gc.collect()  # Trigger garbage collection manually

# Example: Disabling the garbage collector temporarily
gc.disable()  # Disable garbage collection (use cautiously for performance tuning)
# Perform memory-intensive operations here
gc.enable()  # Re-enable garbage collection

# ----------------------------------------------------------------------
# 2. Profiling Code with `cProfile` and `timeit`
# ----------------------------------------------------------------------

# a. Using `cProfile` for Profiling
# The `cProfile` module provides a detailed report of where your program spends time.

# Example: Profiling a function
def slow_function():
    total = 0
    for i in range(10**6):
        total += i
    return total

if __name__ == "__main__":
    import cProfile
    cProfile.run("slow_function()")

# The output shows the function calls, time spent in each function, and other statistics.

# b. Using `timeit` for Benchmarking Small Code Snippets
# The `timeit` module is used to measure the execution time of small code snippets.

import timeit

# Example: Timing a list comprehension vs. a for loop
list_comprehension_time = timeit.timeit("[x**2 for x in range(1000)]", number=1000)
for_loop_time = timeit.timeit("""
result = []
for x in range(1000):
    result.append(x**2)
""", number=1000)

print(f"List comprehension time: {list_comprehension_time:.5f} seconds")
print(f"For loop time: {for_loop_time:.5f} seconds")

# ----------------------------------------------------------------------
# 3. Code Optimization Techniques
# ----------------------------------------------------------------------

# a. Use Built-In Functions
# Built-in functions in Python are implemented in C and are faster than custom loops.

# Example: Using `sum()` instead of a manual loop
nums = range(1, 1000001)
print(sum(nums))  # Faster
print(sum([x for x in nums]))  # Slower due to list comprehension overhead

# b. Avoid Unnecessary Data Structures
# Minimize memory usage by using efficient data structures.

# Example: Use a generator instead of a list for large sequences
squares_gen = (x**2 for x in range(1000))  # Generator expression (memory-efficient)
squares_list = [x**2 for x in range(1000)]  # List comprehension (uses more memory)

print(sys.getsizeof(squares_gen))  # Prints the memory size of the generator
print(sys.getsizeof(squares_list))  # Prints the memory size of the list

# c. Use `join()` for String Concatenation
# Avoid concatenating strings with `+` in loops. Use `join()` instead.

# Example: Efficient string concatenation
strings = ["Hello"] * 1000
concatenated = "".join(strings)  # Faster
# Inefficient approach:
# concatenated = ""
# for s in strings:
#     concatenated += s  # Slower due to repeated allocations

# d. Leverage `NumPy` for Numerical Computations
# Use `numpy` for efficient array operations instead of Python lists.

import numpy as np

# Example: Vectorized operations with NumPy
nums_np = np.arange(1, 1000001)
print(nums_np.sum())  # Much faster than Python's sum for large numerical data

# e. Reduce Function Call Overhead
# Inline calculations or use local variables to minimize function call overhead.

# Example: Using local variables
def optimized_function(nums):
    total = 0
    append = total.__add__  # Assign method to a local variable for faster access
    for num in nums:
        append(num)
    return total

# f. Profile and Optimize Bottlenecks
# Always profile your code to identify bottlenecks before optimizing.

# ----------------------------------------------------------------------
# Final Thoughts and Best Practices
# ----------------------------------------------------------------------

# Summary:
# 1. **Memory Optimization**:
#    - Use `sys.getsizeof()` to measure memory usage of objects.
#    - Use generators for memory-efficient processing of large data sets.
#    - Use `gc` to manage and fine-tune garbage collection.

# 2. **Profiling**:
#    - Use `cProfile` to analyze where your program spends time.
#    - Use `timeit` to benchmark and compare specific code snippets.

# 3. **Code Optimization Techniques**:
#    - Use built-in functions like `sum()`, `max()` for better performance.
#    - Minimize unnecessary data structures.
#    - Prefer generator expressions over list comprehensions for large data.
#    - Leverage libraries like `NumPy` for numerical computations.

# Optimization and profiling are iterative processes. Start by profiling the code,
# identify bottlenecks, and then optimize the critical sections.

