from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, String, Date
from pydantic import BaseModel

class MeetDetails(Base):
    __tablename__ = "meet_details"

    id = Column(Integer, primary_key=True, index=True)
    meet_name = Column(Integer, primary_key=True, index=True)
    host_gym = Column(String(100), nullable=False)
    # director_name = Column(String(100), nullable=False)
    # director_email = Column(String(100), unique=True, nullable=False)
    # facility_name = Column(String(100), nullable=False)
    # facility_address = Column(String(100), nullable=False)
    # facility_city = Column(String(100), nullable=False)
    # facility_state = Column(String(2), nullable=False)
    # facility_zip = Column(Integer, nullable=False)
    # start_date = Column(Date)
    # end_date = Column(Date)

class MeetDetailsCreate(BaseModel):
    meet_name: str
    host_gym: str

class MeetDetailsResponse(BaseModel):
    id: int
    meet_name: str
    host_gym: str

    class Config: 
        from_attributes = True