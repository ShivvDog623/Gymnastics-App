from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, CheckConstraint, UniqueConstraint
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional
from decimal import Decimal
from typing_extensions import Annotated


class MeetEntry(Base):
    __tablename__ = "meet_entry"

    meet_entry_id = Column(Integer, primary_key=True, index=True)

    meet_id = Column(
        Integer,
        ForeignKey("meet_details.meet_id", ondelete="CASCADE"),
        nullable=False
    )

    gymnast_id = Column(
        Integer,
        ForeignKey("gymnast.gymnast_id", ondelete="CASCADE"),
        nullable=False
    )

    session_id = Column(
        Integer,
        ForeignKey("sessions.session_id", ondelete="CASCADE"),
        nullable=False
    )

    team_id = Column(
        Integer,
        ForeignKey("teams.team_id", ondelete="CASCADE"),
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint("meet_id", "gymnast_id", name="uq_meet_gymnast"),
    )


class MeetEntryBase(BaseModel):
    meet_id: int
    gymnast_id: int
    session_id: int
    team_id: int

class MeetEntryCreate(MeetEntryBase):
    pass

class MeetEntryResponse(MeetEntryBase):
    meet_entry_id: int

    class Config:
        from_attributes = True

class MeetEntryJudgeView(BaseModel):
    meet_entry_id: int

class MeetEntryUpdate(BaseModel):
    session_id: Optional[int] = None
    team_id: Optional[int] = None

class MeetEntryLookup(BaseModel):
    meet_id: int
