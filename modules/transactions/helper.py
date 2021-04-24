from datetime import datetime
from sqlalchemy.orm import Session

from . import schemas
from .model import TransactionModel


def create_transaction(transactoin: schemas.TransactionCreateSchema, db: Session):
    new_transaction = TransactionModel(**transactoin.dict())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction


def get_transactions(db: Session):
    return db.query(TransactionModel).all()


def get_transaction_by_id(id_transaction: int, db: Session):
    return (
        db.query(TransactionModel)
        .filter(TransactionModel.id_transaction == id_transaction)
        .first()
    )


def delete_transaction(id_transaction: int, db: Session):
    deleted_transaction = (
        db.query(TransactionModel)
        .filter(TransactionModel.id_transaction == id_transaction)
        .first()
    )
    deleted_transaction.deleted_at = datetime.now()
    db.commit()
    db.refresh(deleted_transaction)
    return deleted_transaction