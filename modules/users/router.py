from typing import List

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import sign_jwt
from app.database import get_db
from . import helper, schemas

users_router = APIRouter(prefix="/users")

users: List[schemas.UserSchema] = []


@users_router.get("/")
async def get_users(db: Session = Depends(get_db)):

    users = helper.get_users(db)
    return users


@users_router.get("/email/{email}")
async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    user_filtered = helper.get_user_by_email(email, db)
    return user_filtered


@users_router.post("/create")
async def create_user(
    user: schemas.UserCreateSchema = Body(...), db: Session = Depends(get_db)
):
    test_users = helper.get_user_by_email(user.email, db)
    if test_users:
        if test_users.deleted_at != None:
            user_reactived = helper.remove_deleted(user.email, db)
            return user_reactived

        return {"Error": "User alredy been registerd"}

    new_user = helper.create_user(user, db)

    return sign_jwt(new_user.id_user)


@users_router.post("/login")
async def login(
    user: schemas.UserLoginSchema = Body(...), db: Session = Depends(get_db)
):
    user_filterd = helper.get_user_by_email(user.email, db)
    authenthication = helper.check_user(user, db)

    if authenthication == "valid":
        gerete_token = sign_jwt(user_filterd.id_user)
        gerete_token["user"] = user_filterd
        return gerete_token
    else:
        return {"error": authenthication}


@users_router.delete("/id/{id_user}")
async def delete_user(id_user: int, db: Session = Depends(get_db)):
    user_deleted = helper.delete_user_by_id(id_user, db)
    return user_deleted
