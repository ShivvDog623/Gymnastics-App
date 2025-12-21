from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, String, Date
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import date
from typing import Annotated, Optional

# Sql Alchemy Model
class MeetDetails(Base):
    __tablename__ = "meet_details"

    meet_id = Column(Integer, primary_key=True, index=True)
    meet_name = Column(String(100), unique=True, index=True)
    host_gym = Column(String(100), nullable=False)
    facility_name = Column(String(100), nullable=False)
    facility_address = Column(String(100), nullable=False)
    facility_city = Column(String(100), nullable=False)
    facility_state = Column(String(2), nullable=False)
    facility_zip = Column(Integer, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    sanction_number = Column(Integer, nullable=False, unique=True)
    sanction_organization = Column(String, nullable=False)
    number_of_judges_per_event = Column(Integer, nullable=False)
    score_entry_or_tie_break_rules = Column(String, nullable=False)

# Pydantic Models
class MeetDetailsBase(BaseModel):
    meet_name: str
    host_gym: str
    facility_name: str
    facility_address: str
    facility_city: str
    facility_state: str
    facility_zip: int
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    sanction_number: int
    sanction_organization: str
    number_of_judges_per_event: int
    score_entry_or_tie_break_rules: str

class MeetDetailsCreate(MeetDetailsBase):
    pass

class MeetDetailsResponse(MeetDetailsBase):
    meet_id: int

    class Config:
        from_attributes = True

class MeetDetailsUpdate(BaseModel):
    meet_name: Optional[str] = None
    host_gym: Optional[str] = None
    facility_name: Optional[str] = None
    facility_address: Optional[str] = None
    facility_city: Optional[str] = None
    facility_state: Optional[str] = None
    facility_zip: Optional[int] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    sanction_number: Optional[int] = None
    sanction_organization: Optional[str] = None
    number_of_judges_per_event: Optional[int] = None
    score_entry_or_tie_break_rules: Optional[str] = None
