from datetime import date

from pydantic import BaseModel


class HomeworkBase(BaseModel):
    name: str
    date_start: date
    date_end: date
    id_subject: int
    subject: int


class Homework(BaseModel):
    id: int

    class Config:
        from_attributes = True
