# import pytest
# from fastapi import FastAPI
# from starlette.testclient import TestClient
#
# from tests.setup import BASE_URL
#
#
# @pytest.fixture(scope="function")
# def setup_app():
#     app = FastAPI()
#     return app
#
#
# @pytest.fixture(scope="function")
# def client(setup_app):
#     return TestClient(setup_app)
#
#
# def test_all_users(client):
#     response = client.get(BASE_URL + "/")
#     print(response)
#     assert response.status_code == 200
#     print(response.json())
#
#
#
