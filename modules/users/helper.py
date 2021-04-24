from datetime import datetime
from typing import List
from sqlalchemy.orm import Session

from .schemas import UserLoginSchema, UserCreateSchema, UserSchema
from .models import UserModel


def check_user(data: UserLoginSchema, db: Session):

    user_looked = (
        db.query(UserModel)
        .filter(UserModel.email == data.email and UserModel.deleted_at == None)
        .first()
    )

    if not user_looked:
        return "Incorrect e-mail"

    if user_looked.password == data.password:
        return "valid"

    else:
        return "Incorrect password"


def create_user(user: UserCreateSchema, db: Session) -> UserSchema:
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db: Session) -> List[UserSchema]:
    return db.query(UserModel).all()


def get_user_by_email(email: str, db: Session) -> UserSchema:
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_user_by_id(id_user: int, db: Session) -> UserSchema:
    return db.query(UserModel).filter(UserModel.email == id_user).first()


def delete_user_by_id(id_user: int, db: Session):
    user_deleted = db.query(UserModel).filter(UserModel.id_user == id_user).first()
    user_deleted.deleted_at = datetime.now()
    user_deleted.updated_at = datetime.now()
    db.commit()
    db.refresh(user_deleted)
    return user_deleted


def remove_deleted(email: str, db: Session):
    user_deleted = db.query(UserModel).filter(UserModel.email == email).first()
    user_deleted.deleted_at = None
    user_deleted.updated_at = datetime.now()
    db.commit()
    db.refresh(user_deleted)
    return user_deleted