import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session

from app.main import app
from app.routers import get_db
from db.database import Base
from models.models import User

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def init_db(db: Session):
    question1 = User(name="What is the capital of France?")
    db.add(question1)

    db.commit()
    db.close()


app.dependency_overrides[get_db] = override_get_db
init_db(TestingSessionLocal())
