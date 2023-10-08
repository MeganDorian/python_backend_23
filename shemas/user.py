from pydantic import BaseModel


class UserSubject(BaseModel):
    id_user: int
    id_subject: int


class UserBase(BaseModel):
    name: str


class User(UserBase):
    id: int
    subjects: list[UserSubject] = []

    class Config:
        orm_mode = True
