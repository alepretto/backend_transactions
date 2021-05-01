from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .auth.auth_bearer import JWTBearer

from modules.users.router import users_router
from modules.stocks.router import stock_router
from modules.transactions.router import transactions_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(users_router)
app.include_router(stock_router) # , dependencies=[Depends(JWTBearer())]
app.include_router(transactions_router)
