# chats/auth.py

from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomJWTAuthentication(JWTAuthentication):
    """Custom wrapper around SimpleJWT authentication."""
    pass
