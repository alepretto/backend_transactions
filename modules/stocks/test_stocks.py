import pytest
from fastapi.testclient import TestClient

from app.database_test import get_cliente_test, get_acess_token
from modules.stocks.schemas import StockSchema


@pytest.fixture
def client():
    client = get_cliente_test()
    return client


def test_create_stock(client: TestClient):
    request_body = {
        "codigo": "BIDI4.SA",
        "descricao": "Banco Inter S.A.",
        "setor": "Financial Services",
        "url": "http://www.bancointer.com.br",
        "logo_url": "https://logo.clearbit.com/bancointer.com.br",
    }

    response = client.post(
        "/stocks/create",
        json=request_body,
        headers={
            "content-type": "application/json",
            "Authorization": get_acess_token(client),
        },
    )

    assert response.status_code == 200

    data_response = response.json()
    data_response = StockSchema(**data_response)

    assert data_response.created_at != None


def test_delete_stock(client: TestClient):
    response = client.get(
        "/stocks",
        headers={
            "content-type": "application/json",
            "Authorization": get_acess_token(client),
        },
    )
    list_stocks = response.json()

    id_stock = next(
        (stock["id_stock"] for stock in list_stocks if stock["codigo"] == "BIDI4.SA")
    )
    response = client.delete(
        f"/stocks/{id_stock}",
        headers={
            "content-type": "application/json",
            "Authorization": get_acess_token(client),
        },
    )
    assert response.status_code == 200

    data_response = StockSchema(**response.json())
    assert data_response.deleted_at != None