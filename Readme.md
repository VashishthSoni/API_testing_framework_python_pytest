# API Testing Framework in Python (Pytest + Requests)

A simple, professional, and resume-ready API testing framework built using **Python**, **Pytest**, and **Requests** library.  
It demonstrates testing REST APIs with GET, POST, PUT, PATCH methods, including authorization, parametrization, logging, and negative scenarios.

---

## Features

- Supports **GET, POST, PUT, PATCH** requests
- Centralized **configuration** (`config.py`) for URL and headers
- **Authorization fixture** for API token
- **Parametrized tests** for multiple scenarios
- **Logging** using Python’s built-in `logging` module with timestamps
- Handles **positive and negative test cases**
- Ready for **data-driven testing** extensions

---

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd api-testing-project
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run Tests
```bash
# Run all tests with logs visible in console
pytest -v --log-cli-level=INFO
```
- -v → verbose output
- --log-cli-level=INFO → shows logger output (request/response logs)

## Example Tests
- GET User by ID (valid/invalid IDs)
- POST Todo (create resource)
- PATCH Todo (partial update)
- Parametrized tests for multiple inputs
- Logs request and response for every test

## Customization
- Update config.py for different environments (dev/stage/prod)
- Replace DEMO_VALID_TOKEN in conftest.py with a real API token
- Add more test modules for additional endpoints
- Extend logging to write into a file if needed

## Tech Stack
- Python 3.x
- Pytest
- Requests library
- Built-in Python logging

## Notes
- Ensure tests/ and helpers/ folders have __init__.py for proper imports
- Always run tests from project root

---