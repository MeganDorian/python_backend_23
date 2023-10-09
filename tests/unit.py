import pytest

from crud.crud import get_users
from tests.setup import TestingSessionLocal


@pytest.fixture(scope="module")
def setup_db():
    db = TestingSessionLocal()
    return db


def test_get_users(setup_db):
    users = get_users(setup_db)
    assert users is not None
    assert len(users) > 0
    assert type(users) is list

