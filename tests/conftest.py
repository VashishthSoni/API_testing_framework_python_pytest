# tests/conftest.py
import pytest
from config import HEADERS  # relative import works with __init__.py

@pytest.fixture
def auth_headers():
    """
    Returns headers with demo Bearer token.
    """
    token = "DEMO_VALID_TOKEN"  # replace with real token if available
    headers = HEADERS.copy()
    headers["Authorization"] = f"Bearer {token}"
    return headers
