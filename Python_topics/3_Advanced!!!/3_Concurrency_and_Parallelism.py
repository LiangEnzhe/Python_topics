# ----------------------------------------------------------------------
# Concurrency and Parallelism in Python
# ----------------------------------------------------------------------
# Python supports different models for running tasks concurrently or in parallel:
# 1. **Multithreading**: Using threads for concurrency (suitable for I/O-bound tasks).
# 2. **Multiprocessing**: Using processes for true parallelism (suitable for CPU-bound tasks).
# 3. **Asyncio**: Using asynchronous programming for efficient I/O-bound tasks.

# ----------------------------------------------------------------------
# 1. Multithreading with `threading`
# ----------------------------------------------------------------------
# Multithreading allows multiple threads to run concurrently within a process.
# Threads share the same memory space, making it ideal for I/O-bound tasks.

import threading
import time

def print_numbers():
    """Function to print numbers from 1 to 5 with a delay."""
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)  # Simulate an I/O operation

def print_letters():
    """Function to print letters from A to E with a delay."""
    for letter in "ABCDE":
        print(f"Letter: {letter}")
        time.sleep(1)  # Simulate an I/O operation

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Multithreading complete.")

# Note: Due to the Global Interpreter Lock (GIL), multithreading does not achieve true parallelism in Python.
# It is suitable for tasks involving I/O (e.g., file reading, network calls).

# ----------------------------------------------------------------------
# 2. Multiprocessing with `multiprocessing`
# ----------------------------------------------------------------------
# Multiprocessing uses separate processes, achieving true parallelism.
# Each process has its own memory space, making it suitable for CPU-bound tasks.

from multiprocessing import Process, current_process

def compute_square(numbers):
    """Function to compute squares of numbers."""
    for n in numbers:
        print(f"{current_process().name} - Square of {n}: {n**2}")

# Define data and processes
numbers = [1, 2, 3, 4, 5]
process1 = Process(target=compute_square, args=(numbers,))
process2 = Process(target=compute_square, args=(numbers,))

# Start processes
process1.start()
process2.start()

# Wait for both processes to complete
process1.join()
process2.join()

print("Multiprocessing complete.")

# Benefits:
# - True parallelism is achieved, as each process runs in its own memory space.
# - Suitable for CPU-intensive tasks like mathematical computations or image processing.

# ----------------------------------------------------------------------
# 3. Asynchronous Programming with `asyncio`
# ----------------------------------------------------------------------
# `asyncio` is a library for writing asynchronous code using `async` and `await`.
# It allows you to run multiple tasks concurrently without using threads or processes.

import asyncio

async def async_print_numbers():
    """Asynchronously print numbers from 1 to 5."""
    for i in range(1, 6):
        print(f"Async Number: {i}")
        await asyncio.sleep(1)  # Non-blocking delay

async def async_print_letters():
    """Asynchronously print letters from A to E."""
    for letter in "ABCDE":
        print(f"Async Letter: {letter}")
        await asyncio.sleep(1)  # Non-blocking delay

async def main():
    # Schedule both tasks to run concurrently
    await asyncio.gather(async_print_numbers(), async_print_letters())

# Run the asyncio event loop
asyncio.run(main())

print("Asyncio complete.")

# Benefits:
# - Ideal for I/O-bound tasks like network calls or database queries.
# - More efficient than threads for handling large numbers of I/O operations.

# ----------------------------------------------------------------------
# Summary: Choosing the Right Model
# ----------------------------------------------------------------------
# 1. **Multithreading**:
#    - Suitable for I/O-bound tasks (e.g., file reading, web scraping).
#    - Limited by the Global Interpreter Lock (GIL), so no true parallelism for CPU-bound tasks.
#    - Use the `threading` module.

# 2. **Multiprocessing**:
#    - Suitable for CPU-bound tasks (e.g., heavy computations, image processing).
#    - Achieves true parallelism as processes have separate memory spaces.
#    - Use the `multiprocessing` module.

# 3. **Asyncio**:
#    - Suitable for I/O-bound tasks that involve many concurrent operations (e.g., web servers).
#    - Uses `async` and `await` for cooperative multitasking.
#    - Use the `asyncio` module for lightweight concurrency without threads or processes.

# ----------------------------------------------------------------------
# Final Notes
# ----------------------------------------------------------------------
# Python provides powerful tools for concurrency and parallelism:
# - Use multithreading for I/O-bound tasks with shared memory.
# - Use multiprocessing for CPU-bound tasks to leverage multiple cores.
# - Use asyncio for lightweight, non-blocking, concurrent I/O operations.

# Choose the right model based on the nature of your task (I/O vs CPU-bound).
