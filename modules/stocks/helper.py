from datetime import datetime
from sqlalchemy.orm import Session

from . import schemas
from .models import StockModel


def create_stock(stock: schemas.StockCreateSchema, db: Session) -> schemas.StockSchema:
    new_stock = StockModel(**stock.dict())
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock


def get_stocks(db: Session):
    return db.query(StockModel).all()


def get_stock_by_codigo(codigo_stock: str, db: Session):
    return db.query(StockModel).filter(StockModel.codigo == codigo_stock).first()


def delete_stock(id_stock: int, db: Session):
    deleted_stock = db.query(StockModel).filter(StockModel.id_stock == id_stock).first()
    deleted_stock.deleted_at = datetime.now()
    deleted_stock.updated_at = datetime.now()
    db.commit()
    db.refresh(deleted_stock)
    return deleted_stock


def reactivate_stock_by_codigo(codigo: str, db: Session):
    deleted_stock = db.query(StockModel).filter(StockModel.codigo == codigo).first()
    deleted_stock.deleted_at = None
    deleted_stock.updated_at = datetime.now()
    db.commit()
    db.refresh(deleted_stock)
    return deleted_stock