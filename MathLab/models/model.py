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

from sqlalchemy.orm import DeclarativeBase, relationship

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


class Chapter(Base):
    __tablename__ = 'chapters'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String)
    order = Column(Integer, unique=True, index=True)
    level_of_education = Column(String)
    disabled = Column(Boolean, default=False)

    tasks = relationship('Task', back_populates="chapter")


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    description = Column(String)
    task_type  = Column(String)
    order = Column(Integer, unique=True, index=True)
    disabled = Column(Boolean, default=False)
    chapter_id = Column(UUID, ForeignKey('chapters.id'))

    examples = relationship('Example', back_populates='task')
    chapter = relationship('Chapter', back_populates='tasks')


class Example(Base):
    __tablename__ = 'examples'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    body = Column(String)
    correct_answer = Column(String)
    explanation = Column(String)
    level = Column(Integer)
    order = Column(Integer, unique=True, index=True)
    disabled = Column(Boolean, default=False)
    task_id = Column(UUID, ForeignKey('tasks.id'))

    steps = relationship('Step', back_populates='example')
    task = relationship('Task', back_populates='examples')
    student_answers = relationship('StudentAnswer', back_populates='example')


class Step(Base):
    __tablename__ = 'steps'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    body = Column(String)
    answers = Column(String)
    #to solve what kind of type should be here (json? 4 different columns for asnswers abcd?)
    correct_answer = Column(String)
    explanation = Column(String)
    order = Column(Integer, unique=True, index=True)
    disabled = Column(Boolean, default=False)
    example_id = Column(UUID, ForeignKey('examples.id'))

    example = relationship('Example', back_populates='examples')
    student_answers = relationship('StudentAnswer', back_populates='step')


class StudentAnswer(Base):
    __tablename__ = 'student_answers'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    student_id = Column(UUID, ForeignKey('students.id'))
    example_id = Column(UUID, ForeignKey('examples.id'), nullable=True)
    step_id = Column(UUID, ForeignKey('steps.id'), nullable=True)
    body = Column(String)
    is_correct = Column(Boolean, nullable=True)
    correct_score = Column(Integer)
    disabled = Column(Boolean, default=False)
    created = Column(Date)

    student = relationship('Student', back_populates='student_answers')
    example = relationship('Example', back_populates='student_answers')
    step = relationship('Step', back_populates='student_answers')
