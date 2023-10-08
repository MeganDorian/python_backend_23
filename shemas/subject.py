from datetime import time

from pydantic import BaseModel

from models.enums import SubjectType, Days
from shemas.homework import Homework


class SubjectBase(BaseModel):
    name: str
    teacher: str
    type: SubjectType
    day: Days
    time_start: time = None
    time_end: time = None


class SubjectCreate(SubjectBase):
    pass


class Subject(SubjectBase):
    id: int
    hws: list[Homework] = []

    class Config:
        from_attributes = True
