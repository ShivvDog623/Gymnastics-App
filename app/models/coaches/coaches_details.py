from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, String, Date, Boolean
from pydantic import BaseModel
from datetime import date
from typing import Optional

# Sql Alchemy Model
class Coaches(Base):
    __tablename__ = 'coaches'
    coach_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    phone_number = Column(Integer, nullable=True)
    email = Column(String, unique=True, nullable=False)
    birth_date = Column(Date, nullable=True)
    pro_expires = Column(Date, nullable=False)
    saftey_expires = Column(Date, nullable=False)
    background_check_expires = Column(Date, nullable=False)
    U100_completed = Column(Boolean, nullable=False)

# Pydantic Model
class CoachBase(BaseModel):
    first_name: str
    last_name: str
    address: Optional[str] = None
    phone_number: Optional[int] = None
    email: str
    birth_date: Optional[date] = None
    pro_expires: date
    saftey_expires: date
    background_check_expires: date
    U100_completed: bool

class CoachCreate(CoachBase):
    pass

class CoachResponse(CoachBase):
    coach_id: int

    class Config:
        from_attributes = True

class CoachUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[int] = None
    email: Optional[str] = None
    birth_date: Optional[date] = None
    pro_expires: Optional[date] = None
    saftey_expires: Optional[date] = None
    background_check_expires: Optional[date] = None
    U100_completed: Optional[bool] = None



