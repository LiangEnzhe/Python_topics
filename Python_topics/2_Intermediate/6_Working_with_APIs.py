# ----------------------------------------------------------------------
# Working with APIs using the `requests` Library
# ----------------------------------------------------------------------
# The `requests` library is a powerful and easy-to-use library for making HTTP requests in Python.
# You can perform CRUD operations (GET, POST, PUT, DELETE) on REST APIs.

import requests  # Import the requests library

# ----------------------------------------------------------------------
# 1. HTTP Requests: GET
# ----------------------------------------------------------------------
# A GET request is used to retrieve data from a server.

# Example: Fetch data from a public API
url = "https://jsonplaceholder.typicode.com/posts/1"  # Example API endpoint
response = requests.get(url)  # Make a GET request
print(response.status_code)  # Prints the HTTP status code (e.g., 200 for success)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data)  # Prints the JSON data as a dictionary
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

# ----------------------------------------------------------------------
# 2. HTTP Requests: POST
# ----------------------------------------------------------------------
# A POST request is used to send data to the server, typically to create a new resource.

# Example: Create a new post
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "New Post",
    "body": "This is the content of the new post.",
    "userId": 1
}
response = requests.post(url, json=payload)  # Send a POST request with JSON data
print(response.status_code)  # Prints the HTTP status code (e.g., 201 for resource created)
print(response.json())  # Prints the server's response as JSON

# ----------------------------------------------------------------------
# 3. HTTP Requests: PUT
# ----------------------------------------------------------------------
# A PUT request is used to update an existing resource.

# Example: Update a post
url = "https://jsonplaceholder.typicode.com/posts/1"
update_payload = {
    "title": "Updated Title",
    "body": "This is the updated content of the post.",
    "userId": 1
}
response = requests.put(url, json=update_payload)  # Send a PUT request with updated data
print(response.status_code)  # Prints the HTTP status code (e.g., 200 for success)
print(response.json())  # Prints the updated resource as JSON

# ----------------------------------------------------------------------
# 4. HTTP Requests: DELETE
# ----------------------------------------------------------------------
# A DELETE request is used to delete a resource on the server.

# Example: Delete a post
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)  # Send a DELETE request
print(response.status_code)  # Prints the HTTP status code (e.g., 200 for success)

if response.status_code == 200:
    print("Resource deleted successfully.")
else:
    print("Failed to delete the resource.")

# ----------------------------------------------------------------------
# 5. Working with JSON Data
# ----------------------------------------------------------------------
# JSON (JavaScript Object Notation) is a popular format for sending and receiving structured data.

# Example: Convert a Python dictionary to a JSON string
import json

python_data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
json_string = json.dumps(python_data)  # Convert to JSON string
print(json_string)  # Prints: {"name": "Alice", "age": 25, "city": "New York"}

# Example: Convert a JSON string to a Python dictionary
json_data = '{"name": "Bob", "age": 30, "city": "Los Angeles"}'
python_dict = json.loads(json_data)  # Parse JSON string into a dictionary
print(python_dict)  # Prints: {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}

# Handling JSON responses from APIs
response = requests.get("https://jsonplaceholder.typicode.com/users/1")
if response.status_code == 200:
    user_data = response.json()  # Parse JSON response
    print(f"User Name: {user_data['name']}")
    print(f"Email: {user_data['email']}")
else:
    print(f"Failed to fetch user data. Status code: {response.status_code}")

# ----------------------------------------------------------------------
# Summary: Best Practices for Working with APIs
# ----------------------------------------------------------------------

# 1. Check the HTTP Status Code
# Always check `response.status_code` to ensure the request was successful.
# - 200: OK
# - 201: Created
# - 404: Not Found
# - 500: Internal Server Error

# 2. Use `response.json()` to Parse JSON
# Most APIs return JSON responses. Use `response.json()` to directly parse them into Python dictionaries.

# 3. Handle Exceptions
# Use `try`/`except` to handle connection issues or other errors.
try:
    response = requests.get("https://jsonplaceholder.typicode.com/invalid_endpoint")
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")

# 4. Use Timeout for Long Requests
# To avoid hanging indefinitely, set a timeout.
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)  # 5-second timeout
except requests.exceptions.Timeout:
    print("The request timed out.")

# 5. Authentication and Headers
# Use headers to send additional information like authentication tokens.
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
response = requests.get("https://api.example.com/secure-data", headers=headers)
print(response.status_code)
