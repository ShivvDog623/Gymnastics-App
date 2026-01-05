from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, ForeignKey, String, UniqueConstraint
from pydantic import BaseModel
from typing import Optional


# Sql Alchemy Model
class Teams(Base):
    __tablename__ = "teams"

    team_id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String, nullable=False, index=True)
    level = Column(String, nullable=True, index=True)
    division = Column(String, nullable=False, index=True)
    external_team_id = Column(Integer, nullable=True, index=True)

    gym_id = Column(
        Integer,
        ForeignKey("gyms.gym_id", ondelete="CASCADE"),
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint("gym_id", "external_team_id", "level", "division",
                        name="uq_team_external_level_division"),
    )

class TeamBase(BaseModel):
    team_name: str
    level: Optional[str] = None
    division: str
    external_team_id: Optional[int] = None
    gym_id: int

class TeamCreate(TeamBase):
    pass

class TeamResponse(TeamBase):
    team_id: int

    class Config:
        from_attributes = True

class TeamUpdate(BaseModel):
    team_name: Optional[str] = None
    level: Optional[str] = None
    division: Optional[str] = None
    external_team_id: Optional[int] = None
    gym_id: Optional[int] = None
