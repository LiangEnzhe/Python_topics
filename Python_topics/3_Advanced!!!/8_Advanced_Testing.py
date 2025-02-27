# ----------------------------------------------------------------------
# Advanced Testing in Python
# ----------------------------------------------------------------------
# Writing robust tests involves:
# 1. Mocking: Replacing parts of your system under test with mock objects.
# 2. Edge Case Testing: Ensuring your code works in unusual or extreme scenarios.
# 3. Continuous Integration and Deployment (CI/CD): Automating testing and deployment workflows.

# ----------------------------------------------------------------------
# 1. Mocking in Unit Testing
# ----------------------------------------------------------------------
# Mocking allows you to simulate the behavior of external dependencies or parts
# of your system for isolated testing.

from unittest.mock import MagicMock, patch
import requests

# a. Example: Mocking an external API call
def fetch_data_from_api(url):
    """Fetch data from an API endpoint."""
    response = requests.get(url)
    return response.json()  # Assume the response is JSON data

# Test case with mocking
@patch("requests.get")  # Mock the `requests.get` method
def test_fetch_data_from_api(mock_get):
    # Define the mock's return value
    mock_get.return_value.json.return_value = {"key": "value"}
    
    # Call the function under test
    url = "https://api.example.com/data"
    result = fetch_data_from_api(url)
    
    # Assert that the mock was called with the correct arguments
    mock_get.assert_called_once_with(url)
    
    # Assert the return value of the function
    assert result == {"key": "value"}

# b. Example: Mocking an object
class Database:
    """A simple database class."""
    def connect(self):
        """Connect to the database."""
        return "Connected"

    def query(self, query):
        """Run a query."""
        return "Query result"

# Test with a mock database
def test_database_query():
    mock_db = MagicMock()
    mock_db.query.return_value = "Mocked result"
    
    result = mock_db.query("SELECT * FROM users")
    assert result == "Mocked result"  # Assert the mocked return value
    mock_db.query.assert_called_once_with("SELECT * FROM users")  # Assert the query was called correctly

# ----------------------------------------------------------------------
# 2. Testing Edge Cases
# ----------------------------------------------------------------------
# Edge cases are unusual or extreme inputs that test the robustness of your code.

# a. Example: Function to divide two numbers
def divide(a, b):
    """Divide two numbers, handling edge cases like division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# Test edge cases
def test_divide():
    # Normal cases
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    
    # Edge case: Division by zero
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!"
    
    # Edge case: Very large numbers
    assert divide(1e10, 2) == 5e9
    
    # Edge case: Very small numbers
    assert divide(1e-10, 2) == 5e-11

# ----------------------------------------------------------------------
# 3. Continuous Integration and Deployment (CI/CD)
# ----------------------------------------------------------------------
# CI/CD automates the process of testing and deploying code.
# - **Continuous Integration (CI)**:
#    Automatically run tests whenever new code is pushed to the repository.
# - **Continuous Deployment (CD)**:
#    Automatically deploy code to production (or staging) after it passes tests.

# Tools commonly used for CI/CD:
# - **GitHub Actions**: Define workflows directly in your repository.
# - **Jenkins**: Highly customizable CI/CD server.
# - **GitLab CI/CD**: Integrated CI/CD tool in GitLab.
# - **CircleCI** or **Travis CI**: Hosted CI/CD solutions.

# Example CI Workflow using GitHub Actions (YAML file in `.github/workflows/ci.yml`):
"""
name: CI Pipeline

on:
  push:
    branches:
      - main  # Run on every push to the `main` branch
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2  # Pull the code from the repo

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9  # Specify Python version

      - name: Install dependencies
        run: |
          pip install -r requirements.txt  # Install project dependencies

      - name: Run tests
        run: |
          pytest  # Run tests using pytest
"""

# ----------------------------------------------------------------------
# Best Practices for Advanced Testing and CI/CD
# ----------------------------------------------------------------------

# 1. **Mock External Dependencies**:
#    - Use `unittest.mock` or `pytest-mock` to replace APIs, databases, or external systems.
#    - Mock objects allow isolated testing of specific components.

# 2. **Test Edge Cases**:
#    - Include tests for unusual or extreme inputs (e.g., empty inputs, large data, invalid formats).
#    - Ensure your code handles edge cases gracefully.

# 3. **Use Fixtures for Test Setup**:
#    - Use `pytest` fixtures to initialize objects or data for tests.
#    - Example:
"""
import pytest

@pytest.fixture
def sample_data():
    return {"key": "value"}  # Sample data for tests

def test_with_fixture(sample_data):
    assert sample_data["key"] == "value"
"""

# 4. **Automate with CI/CD**:
#    - Use tools like GitHub Actions to automate running tests and deploying code.
#    - Define workflows for testing, building, and deploying in YAML files.

# 5. **Fail Fast, Debug Fast**:
#    - Set up your CI pipeline to fail tests immediately on errors.
#    - Review logs for failing test cases and improve code accordingly.

# 6. **Use Test Coverage Tools**:
#    - Use tools like `coverage.py` to measure how much of your code is covered by tests.
#    - Example:
"""
pip install coverage
coverage run -m pytest  # Run tests with coverage tracking
coverage report -m       # Show a coverage report
"""

# ----------------------------------------------------------------------
# Final Thoughts
# ----------------------------------------------------------------------
# Advanced testing ensures robust, reliable, and maintainable code:
# - **Mocking**: Simulate external dependencies for isolated testing.
# - **Edge Case Testing**: Test code in extreme scenarios to avoid surprises in production.
# - **CI/CD**: Automate testing and deployment to ensure rapid and safe code delivery.

# Start with small tests, automate the testing process, and integrate CI/CD for efficient workflows.
