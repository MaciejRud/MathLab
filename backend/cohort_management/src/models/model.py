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

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    name = Column(String)
    last_name = Column(String)
    user_type = Column(String, nullable=False)
    disabled = Column(Boolean, default=False)

    teacher = relationship('Teacher', back_populates='user', uselist=False)
    student = relationship('Student', back_populates='user', uselist=False)


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True)
    user = relationship('User', back_populates='teacher')

    #Specific fields for teachers
    cohorts = relationship('Cohort', back_populates='teacher')


class Student(Base):
    __tablename__ = 'students'

    id = Column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True)
    user = relationship('User', back_populates='student')

    #Specific fields for students
    date_of_birth = Column(Date)
    current_level = Column(Integer)
    cohort_id = Column(UUID, ForeignKey('cohorts.id'))
    cohort = relationship('Cohort', back_populates='students')


class Cohort(Base):
    __tablename__ = 'cohorts'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String)
    teacher_id = Column(UUID, ForeignKey('teachers.id'))
    level_of_education = Column(Integer)

    students = relationship('Student', back_populates='cohort')
    teacher = relationship('Teacher', back_populates='cohorts')





