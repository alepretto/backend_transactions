from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    deleted_at = Column(DateTime)
