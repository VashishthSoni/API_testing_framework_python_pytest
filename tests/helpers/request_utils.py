import requests
from config import BASE_URL, HEADERS

def send_request(method, endpoint, headers=None, **kwargs):
    final_headers = HEADERS.copy()
    if headers:
        final_headers.update(headers)
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.request(method, url, headers=final_headers, timeout=5, **kwargs)
        response.raise_for_status()  # optional: raises for 4xx/5xx
        return response
    except requests.exceptions.RequestException as e:
        # Log the error using logger
        from helpers.logger import logger
        logger.error("Request failed: %s", e)
        raise
