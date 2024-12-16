"""
Security configuration for API.
"""

import os

from fastapi_users.authentication import (
    AuthenticationBackend,
    JWTStrategy,
    BearerTransport
)


SECRET = os.getenv('USER_SECRET')

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

