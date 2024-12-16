"""
Routers for Users management.
"""

from fastapi import APIRouter
from src.auth.config import auth_backend
from src.auth.dependencies import fastapi_users
from src.auth.schemas import UserRead, UserCreate

router = APIRouter()

# Wbudowane endpointy
router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth", tags=["auth"]
)
router.include_router(
    fastapi_users.get_reset_password_router(), prefix="/auth", tags=["auth"]
)
router.include_router(
    fastapi_users.get_verify_router(UserRead), prefix="/auth", tags=["auth"]
)
