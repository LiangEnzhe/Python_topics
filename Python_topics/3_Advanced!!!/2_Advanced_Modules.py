# ----------------------------------------------------------------------
# Advanced Modules in Python
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# 1. argparse: Building Command-Line Tools
# ----------------------------------------------------------------------
# The `argparse` module helps you build command-line tools by parsing command-line arguments.

import argparse

# Example: Command-line tool to perform basic math operations
def main():
    parser = argparse.ArgumentParser(description="A simple math operations CLI tool.")

    # Add arguments to the parser
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"],
                        help="The math operation to perform.")
    parser.add_argument("x", type=float, help="The first number.")
    parser.add_argument("y", type=float, help="The second number.")
    
    # Parse arguments from the command line
    args = parser.parse_args()
    
    # Perform the operation based on the arguments
    if args.operation == "add":
        result = args.x + args.y
    elif args.operation == "subtract":
        result = args.x - args.y
    elif args.operation == "multiply":
        result = args.x * args.y
    elif args.operation == "divide":
        if args.y != 0:
            result = args.x / args.y
        else:
            result = "Error: Division by zero!"
    
    print(f"Result: {result}")

# To test this, save the script and run it from the terminal like:
# python script.py add 5 10
# python script.py divide 10 0

# ----------------------------------------------------------------------
# 2. logging: Creating Robust Logs
# ----------------------------------------------------------------------
# The `logging` module provides a flexible framework for creating logs for debugging and tracking program execution.

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Define the log format
    filename="app.log",  # Write logs to a file
    filemode="w"  # Overwrite the log file (use "a" to append)
)

# Example: Using the logger
def divide(x, y):
    logging.info(f"Dividing {x} by {y}")
    try:
        result = x / y
        logging.info(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero!")
        return "Error: Division by zero!"

print(divide(10, 2))  # Logs and prints: 5.0
print(divide(10, 0))  # Logs and prints: Error: Division by zero!

# Log Levels:
# - DEBUG: Detailed information for debugging.
# - INFO: General information about program execution.
# - WARNING: An indication of something unexpected.
# - ERROR: A more serious problem.
# - CRITICAL: A very serious error.

# ----------------------------------------------------------------------
# 3. os and shutil: File and Directory Management
# ----------------------------------------------------------------------
# The `os` module provides utilities for interacting with the operating system,
# while `shutil` provides high-level file and directory operations.

import os
import shutil

# a. Working with Directories
# Get the current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# Create a new directory
os.makedirs("test_dir", exist_ok=True)  # Creates the directory if it doesn't exist

# List files and directories in a path
print(os.listdir(cwd))  # Prints the contents of the current directory

# Remove a directory
os.rmdir("test_dir")  # Removes the directory (must be empty)

# b. Working with Files
# Create a new file
with open("example.txt", "w") as file:
    file.write("Hello, world!")

# Check if a file exists
if os.path.exists("example.txt"):
    print("File exists.")

# c. shutil for High-Level Operations
# Copy a file
shutil.copy("example.txt", "copy_of_example.txt")  # Copies the file

# Move a file
shutil.move("copy_of_example.txt", "moved_example.txt")  # Moves/renames the file

# Delete a file
os.remove("example.txt")
os.remove("moved_example.txt")

# ----------------------------------------------------------------------
# 4. pathlib: Working with Paths
# ----------------------------------------------------------------------
# The `pathlib` module provides an object-oriented approach to work with file paths.

from pathlib import Path

# a. Creating and Inspecting Paths
# Create a Path object
path = Path("example.txt")

# Check if the path exists
if not path.exists():
    path.write_text("This is an example file.")  # Write text to the file

# Check properties of the path
print(f"Name: {path.name}")  # Prints: example.txt
print(f"Parent Directory: {path.parent}")  # Prints the parent directory
print(f"File Extension: {path.suffix}")  # Prints: .txt
print(f"Is File: {path.is_file()}")  # True if it's a file

# b. Directory Traversal
cwd = Path.cwd()  # Get the current working directory
print(list(cwd.iterdir()))  # List all files and directories in the current directory

# c. Path Operations
# Create a new path
new_path = Path("test_dir/new_file.txt")
new_path.parent.mkdir(parents=True, exist_ok=True)  # Create parent directories if needed
new_path.write_text("This is a new file.")  # Write text to the file

# Read the contents of the file
print(new_path.read_text())  # Prints: This is a new file.

# Clean up
new_path.unlink()  # Deletes the file
new_path.parent.rmdir()  # Deletes the directory

# ----------------------------------------------------------------------
# Summary of Advanced Modules:
# ----------------------------------------------------------------------

# 1. **argparse**:
#    - Build command-line tools with arguments and options.
#    - Use `argparse.ArgumentParser` to define and parse arguments.

# 2. **logging**:
#    - Create robust logs with different levels (DEBUG, INFO, ERROR).
#    - Use `logging.basicConfig()` to configure the logger.

# 3. **os and shutil**:
#    - Use `os` for low-level file/directory management (e.g., creating, deleting).
#    - Use `shutil` for high-level operations (e.g., copying, moving).

# 4. **pathlib**:
#    - Modern, object-oriented path handling.
#    - Provides convenient methods for path manipulation and file operations.

# ----------------------------------------------------------------------
# Final Thoughts
# ----------------------------------------------------------------------
# These modules simplify common tasks and make your programs more efficient:
# - `argparse`: For creating powerful CLI tools.
# - `logging`: For debugging and monitoring program execution.
# - `os` and `shutil`: For file and directory management.
# - `pathlib`: For cleaner and more readable path handling.

