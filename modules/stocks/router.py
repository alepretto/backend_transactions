from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from app.database import get_db
from . import schemas, helper


stock_router = APIRouter(prefix="/stocks")


@stock_router.post("/create")
async def create_stock(
    stock: schemas.StockCreateSchema = Body(...), db: Session = Depends(get_db)
):
    valid_stock = helper.get_stock_by_codigo(stock.codigo, db)
    if valid_stock:
        if valid_stock.deleted_at != None:
            reactivated_stock = helper.reactivate_stock_by_codigo(stock.codigo, db)
            return reactivated_stock

        return {"message": "this stock alredy been registered"}

    return helper.create_stock(stock, db)


@stock_router.get("/")
async def get_stocks(db: Session = Depends(get_db)):
    return helper.get_stocks(db)


@stock_router.delete("/{id_stock}")
async def delete_stock(id_stock: int, db: Session = Depends(get_db)):
    return helper.delete_stock(id_stock, db)