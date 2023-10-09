import pytest

from crud.crud import get_users, get_user_subjects
from tests.setup import TestSessionLocal


@pytest.fixture(scope="module")
def setup_db():
    db = TestSessionLocal()
    return db


def test_get_users(setup_db):
    users = get_users(setup_db)
    assert users is not None
    assert len(users) > 0
    assert type(users) is list


@pytest.mark.parametrize("user_name, id, subject_name", [
    ("Kelvin Kelly", 1, "Rodeo"),
    ("Milly Tompson", 2, "Rodeo")])
def test_user(user_name, id, subject_name, setup_db):
    subjects = get_user_subjects(setup_db, id)
    assert subjects is not None
    assert subjects[0].name == subject_name
