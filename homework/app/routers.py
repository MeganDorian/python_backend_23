import time

from fastapi import APIRouter, status, Body, Path

from homework.db.database import engine, SessionLocal
from homework.models.models import Base
from homework.shemas.user import User, UserBase
from homework.tasks.tasks import longtime_task_example
from homework.tasks import celery

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


@router.post(
    "/users/info", response_model=UserBase, status_code=status.HTTP_201_CREATED
)
def get_random_user_info(user: UserBase = Body()):
    """
    Return next (random for current example) information about user
    """
    res = longtime_task_example.delay(user)
    return User(name=str(res))


@router.get("/users/info/{res}", response_model=UserBase)
def get_user_info(res: int = Path()):
    """
    Return from long task
    """
    res = celery.app.AsyncResult(res)
    if res.state == "SUCCESS":
        result = res.get()
    else:
        result = None
    return UserBase(name=result)
