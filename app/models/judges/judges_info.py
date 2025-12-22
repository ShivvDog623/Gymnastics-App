from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, String, Date, Boolean
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import date
from typing import Annotated, Optional

# Sql Alchecy Model

class Judges(Base):
    __tablename__ = "judges"
    judge_id = Column(Integer, primary_key=True, index=True)
    judge_pro_number = Column(Integer, unique=True, index=True)
    first_name = Column(String, nullable=False, index=True)
    last_name = Column(String, nullable=False, index=True)
    address = Column(String, nullable=True)
    phone_number = Column(Integer, nullable=True)
    email = Column(String, unique=True, nullable=True)
    pro_expires = Column(Date, nullable=False)
    saftey_expires = Column(Date, nullable=False)
    background_check_expires = Column(Date, nullable=False)
    coach_pro_number = Column(Integer, unique=True, nullable=False)
    U100_completed = Column(Boolean, nullable=False)
    activation_number = Column(Integer, unique=True, nullable=False)

# Pyandtic Model

class JudgeBase(BaseModel):
    judge_pro_number: int
    first_name: str
    last_name: str
    address: Optional[str] = None
    phone_number: Optional[int] = None
    email: Optional[str] = None
    pro_expires: date
    saftey_expires: date
    background_check_expires: date
    coach_pro_number: int
    U100_completed: bool
    activation_number: int

class JudgeCreate(JudgeBase):
    pass

class JudgeResponse(JudgeBase):
    judge_id: Optional[int] = None 
    judge_pro_number: Optional[int] = None

    class Config:
        from_attributes = True

class JudgeUpdate(BaseModel):
    judge_pro_number: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[int] = None
    email: Optional[str] = None
    pro_expires: Optional[date] = None
    saftey_expires: Optional[date] = None
    background_check_expires: Optional[date] = None
    coach_pro_number: Optional[int] = None
    U100_completed: Optional[bool] = None
    activation_number: Optional[int] = None
