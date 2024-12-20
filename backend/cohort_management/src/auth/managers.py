"""
Logic of FastAPI Users.
"""

import os

from fastapi_users import BaseUserManager



print(f"USERS_SECRET: {os.getenv('USERS_SECRET')}")  # Debug statement
SECRET = os.getenv('USERS_SECRET', 'default_secret')

class UniversalUserManager(BaseUserManager):

    reset_password_token_secret = SECRET
    verification_token_secret = SECRET
    test_reset_password_token = None


