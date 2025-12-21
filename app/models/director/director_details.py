from app.sql_lite_db.dbsql import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from typing import Optional

# Sql Alchemy Model

class Director(Base):
    __tablename__ = "directors"

    director_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# Pydantic Models

class DirectorBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class DirectorCreate(DirectorBase):
    pass

class DirectorResponse(DirectorBase):
    director_id: int

    class Config:
        from_attributes = True

class DirectorUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None