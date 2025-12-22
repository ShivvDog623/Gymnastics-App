from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from pydantic import BaseModel
from typing import Optional

# Sql Alchemy Model

class Gyms(Base):
    __tablename__ = "gyms"
    gym_id = Column(Integer, primary_key=True, index=True)
    gym_name = Column(String, nullable=False, index=True)
    short_name = Column(String, nullable=True, index=True)
    region = Column(String, nullable=False, index=True)
    phone_number = Column(String, nullable=False, index=True)
    address = Column(String, nullable=False, index=True)
    gym_email = Column(String, unique=True, nullable=False, index=True)

# Pydantic Model

class GymBase(BaseModel):
    gym_name: str
    short_name: Optional[str] = None
    region: str
    phone_number: str
    address: str
    gym_email: str

class GymCreate(GymBase):
    pass

class GymUpdate(BaseModel):
    gym_name: Optional[str] = None
    short_name: Optional[str] = None
    region: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    gym_email: Optional[str] = None


class GymResponse(GymBase):
    gym_id: int

    class Config:
        from_attributes = True

