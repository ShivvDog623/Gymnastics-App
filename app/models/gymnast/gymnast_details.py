from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, String, Date
from pydantic import BaseModel
from datetime import date
from typing import Optional

# Sql Alchemy Model
class Gymnast(Base):
    __tablename__ = "gymnast"

    gymnast_id = Column(Integer, primary_key=True, index=True)
    gymnast_number = Column(Integer, unique=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    birthday = Column(Date, nullable=False)
    events = Column(String, nullable=False)
    gym_id = Column(Integer, nullable=False)
    level = Column(String, nullable=True)
    age = Column(Integer, nullable=False)
    age_division = Column(String, nullable=True)
    usag_number = Column(Integer, unique=True, nullable=False)
    session_id = Column(Integer, nullable=False)
    team_id = Column(Integer, nullable=True)


# Pydantic Models
class GymnastBase(BaseModel):
    gymnast_number: int
    first_name: str
    last_name: str
    birthday: date
    events: str
    gym_id: int
    level: Optional[str] = None
    age: int
    age_division: Optional[str] = None
    usag_number: int
    session_id: int
    team_id: Optional[int] = None

class GymnastCreate(GymnastBase):
    pass

class GymnastResponse(GymnastBase):
    gymnast_id: int    
    class Config: 
        from_attributes = True

class GymnastUpdate(BaseModel):
    gymnast_number: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birthday: Optional[date] = None
    events: Optional[str] = None
    gym_id: Optional[int] = None
    level: Optional[str] = None
    age: Optional[int] = None
    age_division: Optional[str] = None
    usag_number: Optional[int] = None
    session_id: Optional[int] = None
    team_id: Optional[int] = None
