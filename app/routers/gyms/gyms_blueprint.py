from fastapi import APIRouter, HTTPException, Depends
from app.models.gyms.gyms_info import Gyms, GymCreate, GymUpdate, GymResponse
from app.sql_lite_db.dbsql import Session, get_db

# Create the router
gyms_router = APIRouter(prefix="/gyms", tags=["Gyms"])

# Get all gyms
@gyms_router.get("/all", response_model=list[GymResponse])
def get_all_gyms(db: Session = Depends(get_db)):
    return db.query(Gyms).all()

# Get gym by ID
@gyms_router.get("/{gym_id}", response_model=GymResponse)
def get_gyms_by_id(gym_id: int, db: Session = Depends(get_db)):
    gym_info = db.query(Gyms).filter(Gyms.gym_id == gym_id).first()
    if not gym_info:
        raise HTTPException(status_code=404, detail="Event not found")
    return gym_info

# Create new gym
@gyms_router.post("/create", response_model=GymCreate)
def create_gym(create_gym: GymCreate, db: Session = Depends(get_db)):

    if db.query(Gyms).filter(Gyms.gym_email == create_gym.gym_email).first():
        raise HTTPException(status_code=400, detail="Gym email already exists")
    
    # Create new gym
    new_gym = Gyms(**create_gym.model_dump())
    db.add(new_gym)
    db.commit()
    db.refresh(new_gym)
    return new_gym

# Update gym details by id
@gyms_router.put("/update/{gym_id}", response_model=GymResponse)
def update_gym_by_id(
    gym_id: int, 
    update_gym: GymUpdate, 
    db: Session = Depends(get_db)):

    gym_data = db.query(Gyms).filter(Gyms.gym_id == gym_id).first()
    if not gym_data:
        raise HTTPException(status_code=404, detail="Gym does not exist")
    

    data = update_gym.model_dump(exclude_unset=True)


    for field, value in data.items():
        setattr(gym_data, field, value)
    
    db.commit()
    db.refresh(gym_data)
    return gym_data

# Delete gym by event ID
@gyms_router.delete("/delete/{gym_id}")
def delete_gym_id(gym_id: int, db: Session = Depends(get_db)):
    delete_gym = db.query(Gyms).filter(Gyms.gym_id == gym_id).first()
    if not delete_gym:
        raise HTTPException(status_code=404, detail="Gym does not exist")
    db.delete(delete_gym)
    db.commit()
    return delete_gym, {"detail": "Gym deleted!"}