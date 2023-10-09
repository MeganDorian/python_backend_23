import datetime

import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session

from app.main import app
from app.routers import get_db
from db.database import Base
from models.enums import SubjectType, Days
from models.models import User, Subject, UserSubject

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
BASE_URL = "http://127.0.0.1:8000"

engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def test_db():
    try:
        db = TestSessionLocal()
        yield db
    finally:
        db.close()


def init_db(db: Session):
    user = User(name="Kelvin Kelly")
    db.add(user)
    user = User(name="Milly Tompson")
    db.add(user)
    subject = [Subject(name="Rodeo", teacher="Jelly Jam", type=SubjectType.LECTURE, day=Days.FRI,
                       time_start=datetime.time(8, 0, 0), time_end=datetime.time(10, 0, 0)),
               Subject(name="Singing", teacher="Jimmy Jo", type=SubjectType.PRACTICE, day=Days.MON,
                       time_start=datetime.time(10, 30, 0), time_end=datetime.time(12, 0, 0))]
    db.add_all(subject)
    user_sub = [UserSubject(id_user=1, id_subject=1), UserSubject(id_user=2, id_subject=1)]
    db.add_all(user_sub)
    db.commit()
    db.close()


app.dependency_overrides[get_db] = test_db
init_db(TestSessionLocal())
