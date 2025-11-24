from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, String, Date
from pydantic import BaseModel, EmailStr, StringConstraints
from datetime import date
from typing import Annotated


class MeetDetails(Base):
    __tablename__ = "meet_details"

    id = Column(Integer, primary_key=True, index=True)
    meet_name = Column(String(100), unique=True, index=True)
    host_gym = Column(String(100), nullable=False)
    director_name = Column(String(100), nullable=False)
    director_email = Column(String(100), unique=True, nullable=False)
    facility_name = Column(String(100), nullable=False)
    facility_address = Column(String(100), nullable=False)
    facility_city = Column(String(100), nullable=False)
    facility_state = Column(String(2), nullable=False)
    facility_zip = Column(Integer, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
class MeetDetailsCreate(BaseModel):
    meet_name: str
    host_gym: str
    director_name: str
    director_email: EmailStr
    facility_name: str
    facility_address: str
    facility_city: str
    facility_state: Annotated[str, StringConstraints(min_length=2, max_length=2)]
    facility_zip: int
    start_date: date
    end_date:  date
class MeetDetailsResponse(BaseModel):
    id: int
    meet_name: str
    host_gym: str
    director_name: str
    director_email: EmailStr
    facility_name: str
    facility_address: str
    facility_city: str
    facility_state: Annotated[str, StringConstraints(min_length=2, max_length=2)]
    facility_zip: int
    start_date: date
    end_date:  date
    class Config: 
        from_attributes = True
class MeetDetailsUpdate(BaseModel):
    meet_name: str | None = None
    host_gym: str | None = None
    director_name: str | None = None
    director_email: EmailStr | None = None
    facility_name: str | None = None
    facility_address: str | None = None
    facility_city: str | None = None
    facility_state: Annotated[str, StringConstraints(min_length=2, max_length=2)] | None = None
    facility_zip: int | None = None
    start_date: date | None = None
    end_date:  date | None = None