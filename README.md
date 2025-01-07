# Login API Test Script

This repository contains a Python script to automate the testing of a login API using POST requests. The script tests both valid and invalid credentials to verify the API's response status.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed.
- The `requests` library installed. You can install it using the following command:

  ```bash
  pip install requests
Run the script with the following command:

`challengeone.py`

Running test case: Test credentials
Test Passed for testUser: Expected status 200, got 200
Running test case: Invalid credentials
Test Passed for invalidUser: Expected status 401, got 401
