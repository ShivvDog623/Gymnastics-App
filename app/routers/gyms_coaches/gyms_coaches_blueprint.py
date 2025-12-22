from fastapi import APIRouter, HTTPException, Depends
from app.models.gym_coaches.gym_coaches_info import GymCoaches, GymCoachCreate, GymCoachResponse
from app.sql_lite_db.dbsql import Session, get_db

# Create the router
gym_coaches_router = APIRouter(prefix="/gym-coaches", tags=["Gym-Coaches"])

# Get all gym and coach keys
@gym_coaches_router.get("/all", response_model=list[GymCoachResponse])
def get_all_gym_coaches(db: Session = Depends(get_db)):
    return db.query(GymCoaches).all()

# Get gym and coach by gym ID
@gym_coaches_router.get("/gym-id/{gym_id}", response_model=GymCoachResponse)
def get_gym_coaches_gym_by_id(gym_id: int, db: Session = Depends(get_db)):
    gym_coaches_info = db.query(GymCoaches).filter(GymCoaches.gym_id == gym_id).first()
    if not gym_coaches_info:
        raise HTTPException(status_code=404, detail="Data not found")
    return gym_coaches_info

# Get gym and coach by coach pro nnumber
@gym_coaches_router.get("/coach-pro-number/{coach_pro_number}", response_model=GymCoachResponse)
def get_gym_coaches_by_coach_pro_number(coach_pro_number: int, db: Session = Depends(get_db)):
    gym_coaches_info = db.query(GymCoaches).filter(GymCoaches.coach_pro_number == coach_pro_number).first()
    if not gym_coaches_info:
        raise HTTPException(status_code=404, detail="Data not found")
    return gym_coaches_info

# Get gym and coach by both gym id and coach pro nnumber
@gym_coaches_router.get("/{gym_id}/{coach_pro_number}", response_model=GymCoachResponse)
def get_gym_coaches_by_both(gym_id: int,coach_pro_number: int, db: Session = Depends(get_db)):
    
    gym_coaches_info = db.query(GymCoaches).filter(
        GymCoaches.gym_id == gym_id,
        GymCoaches.coach_pro_number == coach_pro_number
    ).first()

    if not gym_coaches_info:
        raise HTTPException(status_code=404, detail="Data not found")
    return gym_coaches_info


# Create new gym and coach key
@gym_coaches_router.post("/create", response_model=GymCoachCreate)
def create_gym_coach(create_gym_coach: GymCoachCreate, db: Session = Depends(get_db)):
    
    # Checks to see if the gym and coach key already exists
    existing_gym_coach = (
        db.query(GymCoaches)
        .filter(
            GymCoaches.gym_id == create_gym_coach.gym_id,
            GymCoaches.coach_pro_number == create_gym_coach.coach_pro_number
        )
        .first()
    )
    
    if existing_gym_coach:
        raise HTTPException(status_code=400, detail="Gym and Coach key already exists")
    
    # Create new gym and coach key
    new_gym_coach = GymCoaches(**create_gym_coach.model_dump())
    db.add(new_gym_coach)
    db.commit()
    db.refresh(new_gym_coach)
    return new_gym_coach


# Delete gym and coach key by coach pro number
@gym_coaches_router.delete("/delete/{coach_pro_number}")
def delete_gym_coach_by_coach_pro_number(coach_pro_number: int, db: Session = Depends(get_db)):
    delete_gym_coach = db.query(GymCoaches).filter(GymCoaches.coach_pro_number == coach_pro_number).first()
    if not delete_gym_coach:
        raise HTTPException(status_code=404, detail="Gym and Coach key does not exist")
    db.delete(delete_gym_coach)
    db.commit()
    return delete_gym_coach, {"detail": "Gym and Coach key deleted!"}