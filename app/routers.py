import time

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from crud.crud import get_users, get_user_subjects, get_homeworks
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


@router.get("/subjects/{subject_id}/homeworks")
def all_homeworks(subject_id: int, db: Session = Depends(get_db)):
    hws = get_homeworks(db, subject_id)
    if hws is None:
        raise HTTPException(status_code=404, detail=f"Subject with id={subject_id} not found")
    return hws
