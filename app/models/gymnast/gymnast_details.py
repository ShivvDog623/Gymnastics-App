from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, String, Date
from pydantic import BaseModel
from datetime import date
from typing import Optional

# Sql Alchemy Model
class Gymnast(Base):
    __tablename__ = "gymnast"

    id = Column(Integer, primary_key=True, index=True)
    gymnast_number = Column(Integer, unique=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    birthday = Column(Date, nullable=False)
    level = Column(String, nullable=False)
    usag_number = Column(Integer, unique=True, index=True)
    session = Column(String, nullable=False)
    events = Column(String, nullable=False)

# Pydantic Models
class GymnastCreate(BaseModel):
    gymnast_number: int
    first_name: str
    last_name: str
    birthday: date
    level: str
    usag_number: int
    session: str
    events: str 

class GymnastResponse(BaseModel):
    id: int
    gymnast_number: int
    first_name: str
    last_name: str
    birthday: date
    level: str
    usag_number: int
    session: str
    events: str 
    
    class Config: 
        from_attributes = True

class GymnastUpdate(BaseModel):
    gymnast_number: int | None = None
    first_name: str | None = None
    last_name: str | None = None
    birthday: date | None = None
    level: str | None = None
    usag_number: int | None = None
    session: str | None = None
    events: str | None = None 
