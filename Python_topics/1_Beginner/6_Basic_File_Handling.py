# ----------------------------------------------------------------------
# Reading and Writing Text Files
# ----------------------------------------------------------------------
# Python provides functions like `open()`, `read()`, and `write()` for file handling.

# 1. Opening a File:
# Use the `open()` function to open a file.
# Syntax: open(filename, mode)
# Modes:
# - 'r': Read (default mode, file must exist)
# - 'w': Write (creates a new file or overwrites if it exists)
# - 'a': Append (adds data to the end of the file without overwriting)
# - 'r+': Read and write

# Example: Writing to a file
with open("example.txt", "w") as file:  # Open in write mode
    file.write("Hello, World!\n")  # Write to the file
    file.write("This is a new line.\n")  # Add another line

# Example: Reading from a file
with open("example.txt", "r") as file:  # Open in read mode
    content = file.read()  # Read the entire file content
    print(content)  # Prints the file's content

# Example: Appending to a file
with open("example.txt", "a") as file:  # Open in append mode
    file.write("Appending this line.\n")  # Add text to the end

# Example: Reading a file line-by-line
with open("example.txt", "r") as file:  # Open in read mode
    for line in file:
        print(line.strip())  # Print each line without extra newline characters

# 2. Working with Modes Safely:
# Always use `with` for opening files. It automatically closes the file after use.

# ----------------------------------------------------------------------
# Working with File Paths
# ----------------------------------------------------------------------
# File paths can be relative or absolute.
# - Relative paths are relative to the current working directory.
# - Absolute paths start from the root of the file system.

# Example of a relative path
with open("data/example.txt", "r") as file:  # 'data/' is a relative path
    print(file.read())

# Example of an absolute path (may differ by OS)
# For Windows: with open("C:\\Users\\User\\Documents\\example.txt", "r") as file:
# For Linux/Mac: with open("/home/user/example.txt", "r") as file:

# 1. Using the `os` module to work with paths
import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# Join paths safely
new_file_path = os.path.join(current_directory, "new_file.txt")
print(f"New File Path: {new_file_path}")

# Check if a file exists
if os.path.exists(new_file_path):
    print("File exists!")
else:
    print("File does not exist!")

# 2. Using the `pathlib` module (modern and preferred for path handling)
from pathlib import Path

# Create a Path object
file_path = Path("example.txt")

# Check if the file exists
if file_path.exists():
    print(f"{file_path} exists.")
else:
    print(f"{file_path} does not exist.")

# Create a new file path
new_path = Path("data") / "example.txt"
print(new_path)  # Prints: data/example.txt
