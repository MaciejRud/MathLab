"""
Schemas for Users Api.
"""

import uuid

from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[uuid.UUID]):
    name: str
    last_name: str
    user_type: str  # 'teacher' or 'student'


class UserCreate(schemas.BaseUserCreate):
    name: str
    last_name: str
    user_type: str  # 'teacher' or 'student'



