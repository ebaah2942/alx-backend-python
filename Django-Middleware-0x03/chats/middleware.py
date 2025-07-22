# chats/middleware.py

from datetime import datetime
import os
import logging

# Define log path relative to the current file (inside the chats app)
log_file = os.path.join(os.path.dirname(__file__), 'requests.log')

logger = logging.getLogger(__name__)
handler = logging.FileHandler(log_file)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        return self.get_response(request)
