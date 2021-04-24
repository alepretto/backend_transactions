from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Tipo(str, Enum):
    outcome = "Outcome"
    income = "Income"


class TransactionSchema(BaseModel):

    id_transaction: int = Field(...)
    descricao: str = Field(...)
    tipo: Tipo = Field(...)
    valor: float = Field(...)
    categoria: str = Field(...)
    id_stock: Optional[int] = Field(...)
    id_user: int = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)
    deleted_at: Optional[datetime] = Field(...)

    class Config:
        orm_mode = True


class TransactionCreateSchema(BaseModel):
    descricao: str = Field(...)
    tipo: Tipo = Field(...)
    valor: float = Field(...)
    categoria: str = Field(...)
    id_stock: Optional[int] = Field(...)
    id_user: int = Field(...)