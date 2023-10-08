import time

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from crud.crud import get_users, get_user_subjects
from db.database import engine, SessionLocal
from models.models import Base
from shemas.subject import Subject, SubjectBase
from shemas.user import User
from models.enums import SubjectType, Days

Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def hello_world():
    """
    Base entry point
    """
    return {"Hello world"}


@router.get("/users", response_model=list[User])
def all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Returns all registered users
    """
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}/subjects", response_model=list[Subject])
def user_subjects(user_id: int, db: Session = Depends(get_db)):
    """
    Returns all subject that user with provided attends
    """
    subjects = get_user_subjects(db, user_id)
    if subjects is None:
        raise HTTPException(status_code=404, detail=f"User with id={user_id} not found")
    return subjects


# @router.post("/subjects/add")
# def add_subject(name: str, teacher: str | None, type: str | None, day: str | None, time_start: str | None,
#                 time_end: str | None):
@router.post("/subjects/add")
def add_subject(sub: SubjectBase):
    pass


@router.get("/subjects/{subject_id}/homeworks")
def all_homeworks(subject_id: int):
    pass

# @router.get("/subjects/get/{name}")
# def get_subject_info(name: str):
#     f"""
#     Get entry point with parameter
#     :return: information about {name} subject
#     """
#     sub = next((subject for subject in subjects if subject.name == name), None)
#     if sub is None:
#         raise HTTPException(status_code=404, detail=f"Subject {name} not found")
#     return {
#         "Subject information: ",
#         f"Name: {sub.name} ",
#         f"Teacher: {sub.teacher}",
#         f"Start date: {sub.start_date}",
#         f"End date: {sub.end_date}",
#     }


# @router.get("/subjects/{name}")
# def get_info_by_field(name: str, field: str):
#     f"""
#     Get entry point with query parameter
#     :return: {field} information about {name} subject
#     """
#     sub = next((subject for subject in subjects if subject.name == name), None)
#     if sub is None:
#         raise HTTPException(status_code=404, detail=f"Subject {name} not found")
#     if not hasattr(sub, field):
#         raise HTTPException(status_code=404, detail=f"There is no field {field}")
#     return {f"Your information: {getattr(sub, field)}"}


# @router.post("/subjects/add")
# def post_subject(sub: SubjectBase):
#     """
#     Post entry point to add new subject with fields from Subject class
#     :param sub: contains new subject information
#     :return: new subject
#     """
#     return sub
