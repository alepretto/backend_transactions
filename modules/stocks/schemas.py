from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class StockSchema(BaseModel):
    id_stock: int = Field(...)
    codigo: str = Field(...)
    descricao: str = Field(...)
    setor: str = Field(...)
    url: Optional[str] = Field(...)
    logo_url: Optional[str] = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)
    deleted_at: Optional[datetime] = Field(...)

    class Config:
        orm_mode = True


class StockCreateSchema(BaseModel):
    codigo: str = Field(...)
    descricao: str = Field(...)
    setor: str = Field(...)
    url: Optional[str] = Field(...)
    logo_url: Optional[str] = Field(...)