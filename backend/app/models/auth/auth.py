from app.extensions import db
from datetime import datetime
from typing import Optional
from sqlalchemy import Column, func, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship



user_role_m2m = db.Table(
    'user_role_lnk',
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('role_id', ForeignKey('role.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'user'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(255))
    last_name: Mapped[Optional[str]] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str]
    location: Mapped[Optional[str]]
    title: Mapped[Optional[str]]
    is_active: Mapped[bool]
    blocked: Mapped[bool]
    roles: Mapped[set['Role']] = relationship(secondary=user_role_m2m, back_populates='users')
    created_at: Mapped[Optional[datetime]] = mapped_column(insert_default=func.now())
    created_by_id: Mapped[Optional[int]]
    updated_at: Mapped[Optional[datetime]] = mapped_column(onupdate=func.now())
    updated_by_id: Mapped[Optional[int]]

    def __repr__(self):
        return f'<User {self.username}>'


class Role(db.Model):
    __tablename__ = 'role'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    code: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    users: Mapped[set['User']] = relationship(secondary=user_role_m2m, back_populates='roles')
    created_at: Mapped[Optional[datetime]] = mapped_column(insert_default=func.now())
    created_by_id: Mapped[Optional[int]]
    updated_at: Mapped[Optional[datetime]] = mapped_column(onupdate=func.now())
    updated_by_id: Mapped[Optional[int]]
    
    def __repr__(self):
        return f'<Role {self.name}>'


