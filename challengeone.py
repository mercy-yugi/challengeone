#one
# Write a simple script in Python to automate the testing of a login API using POST requests. 
# The API accepts a username and password and returns a token upon successful authentication.
#  Include a test case for invalid credentials.

import requests

# Base URL of the login API
BASE_URL = "https://example.com/api/login"

# Test data for test and invalid credentials
test_cases = [
    {
        "username": "testUser",
        "password": "testPassword",
        "expected_status": 200,
        "description": "Test credentials"
    },
    {
        "username": "invalidUser",
        "password": "invalidPassword",
        "expected_status": 401,
        "description": "Invalid credentials"
    }
]

# Function to test login API
def test_login_api(username, password, expected_status):
    response = requests.post(BASE_URL, data={"username": username, "password": password})
    assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"
    print(f"Test Passed for {username}: Expected status {expected_status}, got {response.status_code}")

# Run test cases
for test_case in test_cases:
    print(f"Running test case: {test_case['description']}")
    test_login_api(test_case["username"], test_case["password"], test_case["expected_status"])
