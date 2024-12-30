from app.extensions import db
from datetime import datetime
from typing import Optional
from sqlalchemy import func, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(db.Model):
    __tablename__ = 'user_account'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    first_name: Mapped[Optional[str]] = mapped_column(String(50))
    last_name: Mapped[Optional[str]] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(80))
    password: Mapped[str]
    location: Mapped[Optional[str]]
    title: Mapped[Optional[str]]
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
    updated_at: Mapped[Optional[datetime]] = mapped_column(onupdate=func.now())

    def __repr__(self):
        return f'User >>> {self.username}'
