from fastapi import APIRouter, HTTPException, Depends
from app.models.coaches.coaches_details import Coaches, CoachCreate, CoachResponse, CoachUpdate
from app.sql_lite_db.dbsql import Session, get_db

# Create the router
coach_router = APIRouter(prefix="/coaches", tags=["Coaches"])

# Get all coaches
@coach_router.get("/all", response_model=list[CoachResponse])
def get_all_coaches(db: Session = Depends(get_db)):
    return db.query(Coaches).all()

# Create a new coach
@coach_router.post("/create", response_model=CoachCreate)
def create_coach(coach_data: CoachCreate, db: Session = Depends(get_db)):
    if db.query(Coaches).filter(Coaches.email == coach_data.email).first():
        raise HTTPException(status_code=409, detail="Coach with this email already exists")
    
    new_coach = Coaches(**coach_data.model_dump())
    db.add(new_coach)
    db.commit()
    db.refresh(new_coach)
    return new_coach

# Get coaches by ID
@coach_router.get("/{coach_id}", response_model=CoachResponse)
def get_coach_by_id(coach_id: int, db: Session = Depends(get_db)):
    coach_info = db.query(Coaches).filter(Coaches.coach_id == coach_id).first()
    if not coach_info:
        raise HTTPException(status_code=404, detail="Coach not found")
    return coach_info


# Update coach details by coach_id
@coach_router.put("/update/{coach_id}", response_model=CoachResponse)
def update_coach_by_id(
    coach_id: int, 
    update_coach: CoachUpdate,
    db: Session = Depends(get_db)):

    coach_data = db.query(Coaches).filter(Coaches.coach_id == coach_id).first()
    if not coach_data:
        raise HTTPException(status_code=404, detail="Coach does not exist")
    

    data = update_coach.model_dump(exclude_unset=True)


    for field, value in data.items():
        setattr(coach_data, field, value)
    
    db.commit()
    db.refresh(coach_data)
    return coach_data


# Delete coach by coach number
@coach_router.delete("/delete/{coach_id}")
def delete_coach_by_id(coach_id: int, db: Session = Depends(get_db)):
    delete_coach = db.query(Coaches).filter(Coaches.coach_id == coach_id).first()
    if not delete_coach:
        raise HTTPException(status_code=404, detail="Coach does not exist")
    db.delete(delete_coach)
    db.commit()
    return delete_coach, {"detail": "Coach deleted!"}