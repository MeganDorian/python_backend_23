from datetime import datetime, date

from pydantic import BaseModel


class Subject(BaseModel):
    name: str
    teacher: str
    start: datetime = None
    end: datetime = None


subjects = [
    Subject(
        name="MPP",
        teacher="Roman Elizarov",
        start=date(2023, 9, 2),
        end_date=date.today(),
    ),
    Subject(
        name="Python Backend",
        teacher="Emil Shakirov",
        start=date(2023, 9, 19),
        end=date.today(),
    ),
]
