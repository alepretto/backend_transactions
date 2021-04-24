from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .schemas import TransactionCreateSchema
from app.database import get_db
from . import helper


transactions_router = APIRouter(prefix="/transactions")


@transactions_router.post("/")
async def create_transactino(
    transaction: TransactionCreateSchema, db: Session = Depends(get_db)
):
    new_transaction = helper.create_transaction(transaction, db)
    return new_transaction


@transactions_router.get("/")
async def get_transactions(db: Session = Depends(get_db)):
    return helper.get_transactions(db)


@transactions_router.get("/{id_transaction}")
async def get_transaction_by_id(id_transaction: int, db: Session = Depends(get_db)):
    return helper.get_transaction_by_id(id_transaction, db)


@transactions_router.delete("/{id_transaction}")
async def delete_transactions(id_transaction: int, db: Session = Depends(get_db)):
    return helper.delete_transaction(id_transaction, db)