import logging

# Configure logger once, at module level
logger = logging.getLogger("api_test_logger")
logger.setLevel(logging.INFO)

# Only add handler once
if not logger.hasHandlers():
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

logger.propagate = False  # prevent duplicate logs from root logger

def log_request_response(resp):
    """
    Logs request and response details using Python's built-in logger.
    """
    logger.info("REQUEST METHOD: %s | URL: %s", resp.request.method, resp.request.url)
    logger.info("Request Headers: %s", resp.request.headers)
    if resp.request.body:
        logger.info("Request Body: %s", resp.request.body)

    logger.info("RESPONSE STATUS: %s", resp.status_code)
    logger.info("Response Headers: %s", resp.headers)
    try:
        logger.info("Response Body: %s", resp.json())
    except Exception:
        logger.info("Response Body: %s", resp.text)
