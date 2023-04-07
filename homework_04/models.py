"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, declarative_base


# PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
PG_CONN_URI = "sqlite+aiosqlite:///posts.sqlite3"


engine = create_async_engine(
    PG_CONN_URI,
    echo=True)

Base = declarative_base()

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
Session = async_session


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, default="", server_default="")
    username = Column(String(32), nullable=False, default="", server_default="")
    email = Column(String(128), nullable=False, default="", server_default="")
    posts = relationship("Post", back_populates="user")

    # def __str__(self):
    #     return f'User(id={self.id}, username={self.username!r}, email={self.email}'

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

Base = None
Session = None
