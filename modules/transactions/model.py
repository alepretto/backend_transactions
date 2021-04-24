from datetime import datetime
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.types import DateTime

from app.database import Base

from modules.stocks.models import StockModel
from modules.users.models import UserModel


class TransactionModel(Base):
    __tablename__ = "transactions"

    id_transaction = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(255))
    tipo = Column(String(255))
    valor = Column(Float)
    categoria = Column(String(255))
    id_stock = Column(Integer, ForeignKey("stocks.id_stock"))
    id_user = Column(Integer, ForeignKey("users.id_user"))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    deleted_at = Column(DateTime)

    stock = relationship(StockModel)
    user = relationship(UserModel)