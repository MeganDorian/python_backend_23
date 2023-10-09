import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session

from app.main import app
from app.routers import get_db
from db.database import Base
from models.models import User

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

    db.commit()
    db.close()


app.dependency_overrides[get_db] = test_db
init_db(TestSessionLocal())
