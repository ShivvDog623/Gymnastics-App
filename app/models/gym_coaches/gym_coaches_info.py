from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, ForeignKey
from pydantic import BaseModel
from typing import Optional

# Sql Alchemy Model

class GymCoaches(Base):
    __tablename__ = 'gym_coaches'
    
    gym_id = Column(Integer,
                    ForeignKey("gyms.gym_id", ondelete="CASCADE"),
                    primary_key=True
                    )
    coach_pro_number = Column(
        Integer,
        ForeignKey("coaches.coach_pro_number", ondelete="CASCADE"),
        primary_key=True
    )
                    
# Pydantic Models

class GymCoachBase(BaseModel):
    gym_id: int
    coach_pro_number: int

class GymCoachCreate(GymCoachBase):
    pass

class GymCoachResponse(GymCoachBase):
    class Config:
        from_attributes = True

class GymCoachResponse(GymCoachBase):
    class Config:
        from_attributes = True
