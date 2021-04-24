from types import SimpleNamespace

config = SimpleNamespace(
    **{
        "SECRET": "deff1952d59f883uel260e8683fed21ab0ad9a97723eca4f",
        "ALGORITHM": "HS256",
        "URL_DB_PROD": "postgresql://admin:lagartixa99@localhost:5432/db_prod",
        "URL_DB_HOM": "postgresql://admin:lagartixa99@localhost:5433/db_hom",
    }
)
