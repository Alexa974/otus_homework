from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from .database import db


class Posts(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, default="", server_default="")
    body = Column(String, nullable=False, default="", server_default="")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
