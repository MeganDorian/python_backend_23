from sqlalchemy import Column, Integer, String, Time, Enum, ForeignKey, Date
from sqlalchemy.orm import relationship

from db.database import Base
from models.enums import SubjectType, Days


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    subjects = relationship("UserSubject")


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    teacher = Column(String, index=True)
    type = Column(Enum(SubjectType))
    day = Column(Enum(Days))
    time_start = Column(Time, index=True)
    time_end = Column(Time, index=True)
    hws = relationship("Homework", back_populates="subject")


class UserSubject(Base):
    __tablename__ = "users_subjects"
    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("users.id"))
    id_subject = Column(Integer, ForeignKey("subjects.id"))


class Homework(Base):
    __tablename__ = "homeworks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    date_start = Column(Date, index=True)
    date_end = Column(Date, index=True)
    id_subject = Column(Integer, ForeignKey("subjects.id"))
    subject = relationship("Subject", back_populates="hws")
