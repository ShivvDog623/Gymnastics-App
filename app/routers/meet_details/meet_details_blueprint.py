from fastapi import APIRouter, HTTPException, Depends
from app.models.meet_details.meet_details import MeetDetailsResponse, MeetDetailsCreate, MeetDetails, MeetDetailsUpdate
from app.sql_lite_db.dbsql import Session, get_db

# Create the router
meet_details_router = APIRouter(prefix="/meet", tags=["Details"])

# Get all meets and details
@meet_details_router.get("/all", response_model=list[MeetDetailsResponse])
def get_all(db: Session = Depends(get_db)):
    return db.query(MeetDetails).all()

# Get meet details by ID
@meet_details_router.get("/{meet_id}", response_model=MeetDetailsResponse)
def get_meet_details_by_id(meet_id: int, db: Session = Depends(get_db)):
    meet_details = db.query(MeetDetails).filter(MeetDetails.id == meet_id).first()
    if not meet_details:
        raise HTTPException(status_code=404, detail="Meet details not found")
    return meet_details

# Create new meet
@meet_details_router.post("/create", response_model=MeetDetailsCreate)
def create_meet_details(create_meet: MeetDetailsCreate, db: Session = Depends(get_db)):
    if db.query(MeetDetails).filter(MeetDetails.meet_name == create_meet.meet_name).first():
        raise HTTPException(status_code=404, detail="Meet already exists")
    
    # Create new meet
    new_meet = MeetDetails(**create_meet.model_dump())
    db.add(new_meet)
    db.commit()
    db.refresh(new_meet)
    return new_meet

# Update meet details by ID
@meet_details_router.put("/update/{meet_id}", response_model=MeetDetailsResponse)
def update_meet_details(
    meet_id: int, 
    update_meet: MeetDetailsUpdate, 
    db: Session = Depends(get_db)):

    meet_details = db.query(MeetDetails).filter(MeetDetails.id == meet_id).first()
    if not meet_details:
        raise HTTPException(status_code=404, detail="Meet does not exist")
    

    data = update_meet.model_dump(exclude_unset=True)


    for field, value in data.items():
        setattr(meet_details, field, value)
    
    db.commit()
    db.refresh(meet_details)
    return meet_details

# Delete meet by ID
@meet_details_router.delete("/delete/{meet_id}")
def create_meet_details(meet_id: int, db: Session = Depends(get_db)):
    delete_meet = db.query(MeetDetails).filter(MeetDetails.id == meet_id).first()
    if not delete_meet:
        raise HTTPException(status_code=404, detail="Meet does not exist")
    db.delete(delete_meet)
    db.commit()
    return delete_meet, {"detail": "Meet deleted!"}

