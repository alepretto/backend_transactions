import pytest

from app.database_test import get_cliente_test, get_acess_token
from modules.users.schemas import UserSchema


@pytest.fixture
def client():
    client = get_cliente_test()
    return client


def test_create_user(client):

    request_body = {
        "fullname": "Teste",
        "email": "teste@example.com",
        "password": "1234",
    }
    response = client.post("/users/create", json=request_body)
    assert response.status_code == 200


def test_login(client):
    request_body = {
        "email": "teste@example.com",
        "password": "1234",
    }
    response = client.post("/users/login", json=request_body)
    data_response = response.json()

    client.headers["Authorization"] = f"Bearer {data_response['acess_token']}"

    assert response.status_code == 200
    assert isinstance(data_response["acess_token"], str)
    assert UserSchema(**data_response["user"])


def test_delete_user(client):
    response_users = client.get(
        "/users",
        headers={
            "content-type": "application/json",
            "Authorization": get_acess_token(client),
        },
    )
    list_users = response_users.json()
    id_user = next(
        (
            usuario["id_user"]
            for usuario in list_users
            if usuario["email"] == "teste@example.com"
        )
    )

    response = client.delete(f"users/id/{id_user}")
    data_response = response.json()
    assert response.status_code == 200
    assert data_response["deleted_at"] != None
