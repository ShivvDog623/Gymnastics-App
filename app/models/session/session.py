from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, CheckConstraint, UniqueConstraint, Date, Time
from pydantic import BaseModel, Field
from datetime import date, time
from typing import Optional
from typing_extensions import Annotated

# SQL Alchemy Model

class Sessions(Base):
    __tablename__ = "sessions"

    session_id = Column(Integer, primary_key=True, index=True)
    session_number = Column(Integer, nullable=False, index=True)
    session_description = Column(String, nullable=True, index=True)
    session_date = Column(Date, nullable=False, index=True)
    open_warmup = Column(Time, nullable=True)
    timed_warmup = Column(Time, nullable=True)
    march_in = Column(Time, nullable=True)
    awards = Column(Time, nullable=True)
    event_group = Column(String, nullable=True)
    number_of_flights = Column(Integer, nullable=True)
    rotation_type = Column(String, nullable=True)

    meet_id = Column(Integer,
                    ForeignKey("meet_details.meet_id", ondelete="CASCADE"),
                    nullable=False
                    )


# Pydantic

class SessionBase(BaseModel):
    meet_id: int
    session_number: int
    session_description: Optional[str] = None

    session_date: date

    open_warmup: Optional[time] = None
    timed_warmup: Optional[time] = None
    march_in: Optional[time] = None
    awards: Optional[time] = None

    event_group: Optional[str] = None
    number_of_flights: Optional[int] = None
    rotation_type: Optional[str] = None


class SessionCreate(SessionBase):
    pass

class SessionResponse(SessionBase):
    session_id: int

    class Config:
        from_attributes = True

class SessionUpdate(BaseModel):
    session_number: Optional[int] = None
    session_description: Optional[str] = None
    session_date: Optional[date] = None

    open_warmup: Optional[time] = None
    timed_warmup: Optional[time] = None
    march_in: Optional[time] = None
    awards: Optional[time] = None

    event_group: Optional[str] = None
    number_of_flights: Optional[int] = None
    rotation_type: Optional[str] = None
