from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from typing import Optional

# Sql Alchemy Model

class Events(Base):
    __tablename__ = 'events'

    event_id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, nullable=False, index=True)
    gender = Column(String, nullable=False, index=True)
    order_index = Column(Integer, nullable=False, index=True)
    

# Pydantic Model
class EventBase(BaseModel):
    event_name: str
    gender: str
    order_index: int

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    event_name: Optional[str] = None
    gender: Optional[str] = None
    order_index: Optional[int] = None

class EventResponse(EventBase):
    event_id: int

    class Config:
        from_attributes = True
