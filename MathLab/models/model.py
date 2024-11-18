'''
Databases models for Api.
'''

import uuid

from sqlalchemy import (
    Column,
    String,
    Integer,
    UUID,
    Date,
    Boolean,
    Table,
    Enum,
)

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    name = Column(String)
    surname = Column(String)
    disabled = Column(Boolean, default=False)
