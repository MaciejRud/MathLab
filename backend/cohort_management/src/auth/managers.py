"""
Logic of FastAPI Users.
"""

import os

from fastapi_users import BaseUserManager



SECRET = os.getenv('USER_SECRET')

class UniversalUserManager(BaseUserManager):

    reset_password_token_secret = SECRET
    verification_token_secret = SECRET
    test_reset_password_token = None


