# chats/middleware.py

from datetime import datetime, timedelta
import os
import logging
from django.http import HttpResponseForbidden
from collections import defaultdict
from django.http import JsonResponse

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
    
class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour

        # Allow access only between 18:00 (6PM) and 21:00 (9PM)
        if request.path.startswith('/chats/'):
            if not (18 <= current_hour < 21):
                return HttpResponseForbidden("<h1>403 Forbidden</h1><p>Chat access is only allowed between 6PM and 9PM.</p>")

        return self.get_response(request)
    

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Track request timestamps by IP
        self.ip_request_log = defaultdict(list)

    def __call__(self, request):
        ip = self.get_client_ip(request)

        if request.path.startswith('/chats/') and request.method == 'POST':
            now = datetime.now()
            one_minute_ago = now - timedelta(minutes=1)

            # Filter out old timestamps (older than 1 min)
            self.ip_request_log[ip] = [t for t in self.ip_request_log[ip] if t > one_minute_ago]

            if len(self.ip_request_log[ip]) >= 5:
                return JsonResponse({
                    "error": "Rate limit exceeded. You can only send 5 messages per minute."
                }, status=429)

            # Log this request time
            self.ip_request_log[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        """Get the client's real IP address."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
