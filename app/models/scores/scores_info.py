from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, CheckConstraint, UniqueConstraint
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional
from decimal import Decimal
from typing_extensions import Annotated


# Sql Alchemy Model

class Scores(Base):
    __tablename__ = "scores"

    score_id = Column(Integer, primary_key=True, index=True)
    gymnast_id = Column(Integer, ForeignKey("gymnast.gymnast_id"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.event_id"), nullable=False)
    judge_id = Column(Integer, ForeignKey("judges.judge_id"), nullable=False)
    meet_id = Column(Integer, ForeignKey("meet_details.meet_id"), nullable=False)
    
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    # Checks to ensure score is in valid range
    score = Column(
        Numeric(5, 3),
        CheckConstraint("score >= 0 AND score <= 10"),
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint(
            "gymnast_id",
            "event_id",
            "judge_id",
            "meet_id",
            name="uq_score_judge_event_meet"
        ),
    )



ScoreDecimal = Annotated[
    Decimal,
    Field(max_digits=5, decimal_places=3, ge=0, le=10)
]

class ScoreBase(BaseModel):
    event_id: int
    judge_id: int
    meet_id: int
    score: ScoreDecimal

class ScoreCreate(ScoreBase):
    usag_number: int
    pass

class ScoreResponse(ScoreBase):
    score_id: int
    gymnast_id: int
    event_id: int
    judge_id: int
    meet_id: int
    score: ScoreDecimal
    updated_at: datetime


    class Config:
        from_attributes = True

class ScoreCreateByUsag(BaseModel):
    usag_number: int
    event_id: int
    judge_id: int
    meet_id: int
    score: ScoreDecimal

class ScoreUpdate(BaseModel):
    score: Optional[ScoreDecimal] = None
