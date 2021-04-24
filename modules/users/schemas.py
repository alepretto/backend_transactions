from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    id_user: int
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
