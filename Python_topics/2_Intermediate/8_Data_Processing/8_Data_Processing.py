# ----------------------------------------------------------------------
# Data Processing with CSV, JSON, and XML
# ----------------------------------------------------------------------
# In Python, we often need to work with various data formats like CSV, JSON, and XML.
# These formats are commonly used for storing and exchanging data.
# The following examples show how to read, write, and process each format using their respective libraries.

import csv  # CSV library
import json  # JSON library
import xml.etree.ElementTree as ET  # XML library

# ----------------------------------------------------------------------
# 1. CSV Files
# ----------------------------------------------------------------------
# CSV (Comma Separated Values) files are widely used for tabular data storage.
# Python's `csv` module makes it easy to read and write CSV files.

# a. Writing to a CSV File
# Example: Writing a list of dictionaries to a CSV file
data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]

# Specify the CSV file and write data
with open('people.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
    writer.writeheader()  # Write the header row
    writer.writerows(data)  # xWrite the rows of data

# b. Reading from a CSV File
# Example: Reading data from a CSV file into a list of dictionaries
with open('people.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # Prints each row as a dictionary

# ----------------------------------------------------------------------
# 2. JSON Files
# ----------------------------------------------------------------------
# JSON (JavaScript Object Notation) is a lightweight data-interchange format.
# Python's `json` module provides methods to work with JSON data.

# a. Writing to a JSON File
# Example: Writing a Python dictionary to a JSON file
data = {
    "employees": [
        {"name": "Alice", "age": 25, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]
}

# Writing the data to a JSON file
with open('employees.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)  # `indent` makes the JSON human-readable

# b. Reading from a JSON File
# Example: Reading data from a JSON file into a Python dictionary
with open('employees.json', 'r') as json_file:
    data = json.load(json_file)
    print(data)  # Prints the Python dictionary containing the JSON data

# ----------------------------------------------------------------------
# 3. XML Files
# ----------------------------------------------------------------------
# XML (Extensible Markup Language) is used for structured data storage.
# Python's `xml.etree.ElementTree` module helps parse and create XML data.

# a. Writing to an XML File
# Example: Writing structured data into an XML file
root = ET.Element("employees")  # Create root element
employee1 = ET.SubElement(root, "employee", id="1")
ET.SubElement(employee1, "name").text = "Alice"
ET.SubElement(employee1, "age").text = "25"
ET.SubElement(employee1, "city").text = "New York"

employee2 = ET.SubElement(root, "employee", id="2")
ET.SubElement(employee2, "name").text = "Bob"
ET.SubElement(employee2, "age").text = "30"
ET.SubElement(employee2, "city").text = "Los Angeles"

tree = ET.ElementTree(root)  # Create the tree structure
tree.write("employees.xml", encoding="utf-8", xml_declaration=True)

# b. Reading from an XML File
# Example: Reading data from an XML file
tree = ET.parse('employees.xml')
root = tree.getroot()  # Get the root element of the XML
for employee in root.findall('employee'):
    name = employee.find('name').text
    age = employee.find('age').text
    city = employee.find('city').text
    print(f"Name: {name}, Age: {age}, City: {city}")

# ----------------------------------------------------------------------
# Summary of File Formats
# ----------------------------------------------------------------------
# 1. **CSV** (Comma Separated Values):
#    - Ideal for tabular data (rows and columns).
#    - Use the `csv` module to read/write CSV files.
#    - Data is often in a simple text-based table format.
#    - Can be read/written as lists or dictionaries.

# 2. **JSON** (JavaScript Object Notation):
#    - Lightweight format for data interchange.
#    - Python's `json` module is used to read/write JSON data (dictionary format).
#    - Supports nested structures like lists and dictionaries.
#    - Commonly used for APIs and web-based data storage.

# 3. **XML** (Extensible Markup Language):
#    - Structured and self-descriptive format, used for more complex data.
#    - Python's `xml.etree.ElementTree` is used to parse and create XML data.
#    - Data is stored as hierarchical tree structures (elements and attributes).
#    - Often used for configuration files, data exchange, etc.
