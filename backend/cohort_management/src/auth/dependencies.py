'''
Dependencies for fastapi Users.
'''

import uuid

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users.db import SQLAlchemyUserDatabase
from src.utils.database import get_db
from src.models.model import User, Teacher, Student
from src.auth.managers import UniversalUserManager
from src.auth.config import auth_backend
from fastapi_users import FastAPIUsers


async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UniversalUserManager(user_db)


fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)

async def get_current_teacher(current_user: User = Depends(fastapi_users.current_user())):
    if current_user.user_type != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You must be a teacher to access this resource"
        )
    teacher = await Teacher.get(current_user.id)
    if not teacher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found"
        )
    return teacher


async def get_current_student(current_user: User = Depends(fastapi_users.current_user())):
    if current_user.user_type != "student":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You must be a student to access this resource"
        )
    student = await Student.get(current_user.id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return student
