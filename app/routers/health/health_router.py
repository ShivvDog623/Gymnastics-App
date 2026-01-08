from fastapi import APIRouter, Depends
from sqlalchemy import text
from app.sql_lite_db.dbsql import Session, get_db


health_router = APIRouter(prefix="/health", tags=["Health"])

@health_router.get("/")
def health_check():
    return {"status": "ok"}


@health_router.get("/postgres")
def postgres_health(db: Session = Depends(get_db)):
    db.execute(text("SELECT version()"))
    return {"ok": True}