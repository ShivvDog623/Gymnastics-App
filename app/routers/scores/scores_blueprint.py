from fastapi import APIRouter, HTTPException, Depends
from app.models.scores.scores_info import Scores, ScoreCreate, ScoreResponse, ScoreUpdate, ScoreCreateByUsag
from app.sql_lite_db.dbsql import Session, get_db
from app.models.gymnast.gymnast_details import Gymnast
from app.models.judges.judges_info import Judges
from app.dependencies.auth import get_current_judge

# Create the router
scores_router = APIRouter(prefix="/scores", tags=["Scores"])

# Get all scores
@scores_router.get("/all", response_model=list[ScoreResponse])
def get_all_scores(db: Session = Depends(get_db)):
    return db.query(Scores).all()

# Get score by ID
@scores_router.get("/{score_id}", response_model=ScoreResponse)
def get_score_by_id(score_id: int, db: Session = Depends(get_db)):
    score_info = db.query(Scores).filter(Scores.score_id == score_id).first()
    if not score_info:
        raise HTTPException(status_code=404, detail="Score not found")
    return score_info

# Create new score
@scores_router.post("/create/{meet_id}/events/{event_id}", response_model=ScoreResponse)
def create_score(meet_id: int, event_id: int,create_score: ScoreCreateByUsag, db: Session = Depends(get_db), current_judge: Judges = Depends(get_current_judge)):
    
    # Checks to see if the score already exists
    gymnast = (
        db.query(Gymnast)
        .filter(
            Gymnast.usag_number == create_score.usag_number
        )
        .first()
    )

    if not gymnast:
        raise HTTPException(status_code=404, detail="Gymnast not found")
    
    existing_score = (db.query(Scores)
                    .filter(
                    Scores.gymnast_id == gymnast.gymnast_id,
    ).first())

    if existing_score:
        raise HTTPException(status_code=400, detail="Gymnast score already exists")
    
    # Create new score using internal id
    new_score = Scores(
        gymnast_id=gymnast.gymnast_id,
        event_id=event_id,
        judge_id=current_judge.judge_id,
        meet_id=meet_id,
        score=create_score.score,
    )
    db.add(new_score)
    db.commit()
    db.refresh(new_score)
    return new_score

# Update score details by id
@scores_router.put("/update/{score_id}", response_model=ScoreResponse)
def update_score_by_id(
    score_id: int, 
    update_score: ScoreUpdate, 
    db: Session = Depends(get_db)):

    score_data = db.query(Scores).filter(Scores.score_id == score_id).first()
    if not score_data:
        raise HTTPException(status_code=404, detail="Gymnast score does not exist")
    

    data = update_score.model_dump(exclude_unset=True)


    for field, value in data.items():
        setattr(score_data, field, value)
    
    db.commit()
    db.refresh(score_data)
    return score_data

# Delete event by event ID
@scores_router.delete("/delete/{score_id}")
def delete_event_by_id(score_id: int, db: Session = Depends(get_db)):
    delete_score = db.query(Scores).filter(Scores.score_id == score_id).first()
    if not delete_score:
        raise HTTPException(status_code=404, detail="Gymnast score does not exist")
    db.delete(delete_score)
    db.commit()
    return delete_score, {"detail": "Gymnast score deleted!"}