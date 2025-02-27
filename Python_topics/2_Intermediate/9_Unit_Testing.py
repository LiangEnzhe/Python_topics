# ----------------------------------------------------------------------
# Unit Testing in Python
# ----------------------------------------------------------------------
# Unit testing involves testing individual units or components of code to ensure 
# that they perform as expected. In Python, there are multiple ways to write and run 
# unit tests, with `unittest` and `pytest` being the two most popular testing frameworks.

# Testing frameworks like `unittest` or `pytest` help automate the testing process 
# and make it easier to verify that the code behaves as expected.

# We'll also cover **mocking** and **patching**, which are techniques to simulate 
# or replace certain parts of your code during testing.

# ----------------------------------------------------------------------
# 1. Unit Testing with `unittest`
# ----------------------------------------------------------------------
# The `unittest` module provides a framework for writing and running tests in Python.
# It allows you to group related tests, run them, and check if they pass or fail.

import unittest

# Example: A simple function to be tested
def add(a, b):
    """Function that returns the sum of two numbers."""
    return a + b

# a. Writing a Test Case with `unittest`
class TestMathOperations(unittest.TestCase):
    """Test case for math operations."""
    
    def test_add(self):
        """Test the 'add' function."""
        self.assertEqual(add(2, 3), 5)  # Asserts that 2 + 3 equals 5
        self.assertEqual(add(-1, 1), 0)  # Tests negative numbers
        self.assertEqual(add(0, 0), 0)  # Tests adding zeros
    
    def test_add_invalid(self):
        """Test for invalid inputs."""
        with self.assertRaises(TypeError):  # Expect a TypeError for non-numeric input
            add("2", 3)

# Running the test suite
if __name__ == "__main__":
    unittest.main()  # Runs all test cases

# ----------------------------------------------------------------------
# 2. Unit Testing with `pytest`
# ----------------------------------------------------------------------
# `pytest` is a third-party testing library that simplifies writing and running tests.
# It is easier to use and requires less boilerplate code than `unittest`.

# a. Writing a Test Case with `pytest`
# Example: A simple function to be tested
def multiply(a, b):
    """Function that returns the product of two numbers."""
    return a * b

# Simple pytest test function
def test_multiply():
    assert multiply(2, 3) == 6  # Asserts that 2 * 3 equals 6
    assert multiply(-1, 1) == -1  # Tests negative numbers
    assert multiply(0, 0) == 0  # Tests multiplying by zero

# To run the test, use `pytest` from the command line: `pytest test_file.py`

# ----------------------------------------------------------------------
# 3. Mocking and Patching in Unit Tests
# ----------------------------------------------------------------------
# Mocking is a technique used to simulate the behavior of complex objects during testing.
# This allows you to isolate specific parts of your code and control their behavior.

# Mocking is commonly done with the `unittest.mock` module or `pytest-mock` plugin for `pytest`.

# a. Mocking with `unittest.mock`
from unittest.mock import MagicMock

# Example: Mocking an external API call
class WeatherService:
    def get_temperature(self, city):
        """Simulates an API call to get the temperature of a city."""
        # In a real scenario, this might fetch data from an external API
        return 25  # Placeholder for the actual API response

# b. Test Case Using Mock
class TestWeatherService(unittest.TestCase):
    def test_get_temperature(self):
        # Create a mock object of WeatherService
        mock_weather_service = MagicMock()
        
        # Define what the mock should return when `get_temperature` is called
        mock_weather_service.get_temperature.return_value = 30
        
        # Test if the mocked function returns the expected value
        self.assertEqual(mock_weather_service.get_temperature("New York"), 30)
        mock_weather_service.get_temperature.assert_called_with("New York")  # Check if the method was called with the expected argument

# c. Using `patch` to Mock Objects or Methods
from unittest.mock import patch

# Example: Patching an external function call in a method
class DataFetcher:
    def fetch_data(self):
        """Simulates fetching data from an external source."""
        return "Real data from the source."

    def process_data(self):
        """Processes the fetched data."""
        data = self.fetch_data()  # Normally calls fetch_data
        return f"Processed {data}"

# Using `patch` to mock `fetch_data` in the test
class TestDataFetcher(unittest.TestCase):
    @patch.object(DataFetcher, 'fetch_data', return_value="Mocked data")
    def test_process_data(self, mock_fetch):
        data_fetcher = DataFetcher()
        processed_data = data_fetcher.process_data()  # Calls the mocked fetch_data method
        self.assertEqual(processed_data, "Processed Mocked data")  # Check if processing works with mocked data

# Running the test suite
if __name__ == "__main__":
    unittest.main()

# ----------------------------------------------------------------------
# 4. Mocking with `pytest` and `pytest-mock`
# ----------------------------------------------------------------------
# `pytest` provides the `pytest-mock` plugin to handle mocking in an easier way.

# Example: Mocking a function with `pytest-mock`
import requests

def get_website_data(url):
    """Function to fetch website data."""
    response = requests.get(url)
    return response.text

# Test: Mocking `requests.get` with pytest-mock
def test_get_website_data(mocker):
    mock_get = mocker.patch('requests.get', return_value=MagicMock(text="Mocked data"))
    
    result = get_website_data("https://example.com")
    assert result == "Mocked data"  # Check if the mocked data is returned
    mock_get.assert_called_with("https://example.com")  # Check if the URL was passed correctly

# To run the test, use `pytest test_file.py`

# ----------------------------------------------------------------------
# Best Practices for Unit Testing
# ----------------------------------------------------------------------
# 1. **Write small, isolated tests**: Each test should check one specific aspect of your code.
# 2. **Mock external dependencies**: Use mocking to avoid hitting external services, databases, or APIs in unit tests.
# 3. **Use assert methods**: Use assert methods like `assertEqual`, `assertTrue`, and `assertRaises` to validate the outcomes.
# 4. **Keep tests fast**: Unit tests should run quickly. Avoid long-running operations like network requests.
# 5. **Clear and descriptive test names**: Make sure your test names describe the behavior being tested.
