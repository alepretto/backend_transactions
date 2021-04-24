from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime


from app.database import Base


class StockModel(Base):
    __tablename__ = "stocks"

    id_stock = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(255))
    descricao = Column(String(1000))
    setor = Column(String(255))
    url = Column(String(255))
    logo_url = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    deleted_at = Column(DateTime)
