"""
Security configuration for API.
"""

import os

from fastapi_users.authentication import (
    AuthenticationBackend,
    JWTStrategy,
    BearerTransport
)

print(os.getenv('USERS_SECRET'))  # Debug statement
print(f"USERS_SECRET: {os.getenv('USERS_SECRET')}")  # Debug statement
SECRET = os.getenv('USERS_SECRET', 'default_secret')

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

