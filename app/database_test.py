from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .database import Base, get_db
from .app import app
from local_env import config


def get_cliente_test():
    engine_test = create_engine(config.URL_DB_HOM)
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine_test
    )

    Base.metadata.create_all(bind=engine_test)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    client = TestClient(app)
    return client


def get_acess_token(client):
    request_body = {
        "email": "teste@example.com",
        "password": "1234",
    }
    response = client.post("/users/login", json=request_body)

    data_response = response.json()
    return f"Bearer {data_response['acess_token']}"