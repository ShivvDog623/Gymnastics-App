from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.sql_lite_db.dbsql import get_db
from app.models.judges.judges_info import Judges

def get_current_judge(db : Session = Depends(get_db)):
    """
    TODO: Temporary Version
    Always returns Judge with ID = 1
    Replace with real auth JWT later
    """

    judge = (db.query(Judges).filter(Judges.judge_id == 1).first())
    
    if not judge:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Judge not authenticated",
        )

    return judge