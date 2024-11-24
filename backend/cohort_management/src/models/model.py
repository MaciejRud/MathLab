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
    ForeignKey
)

from sqlalchemy.orm import relationship, declarative_base

from src.utils.database import metadata_obj

Base = declarative_base(metadata=metadata_obj)


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    name = Column(String)
    surname = Column(String)
    disabled = Column(Boolean, default=False)

    cohorts = relationship('Cohort', back_populates='teacher')


class Cohort(Base):
    __tablename__ = 'cohorts'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String)
    teacher_id = Column(UUID, ForeignKey('teachers.id'))
    level_of_education = Column(Integer)

    students = relationship('Student', back_populates='cohort')
    teacher = relationship('Teacher', back_populates='cohorts')

class Student(Base):
    __tablename__ = 'students'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    name = Column(String)
    surname = Column(String)
    date_of_birth = Column(Date)
    current_level = Column(Integer)
    disabled = Column(Boolean, default=False)
    cohort_id = Column(UUID, ForeignKey('cohorts.id'))

    cohort = relationship('Cohort', back_populates='students')



