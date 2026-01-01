from fastapi import APIRouter, HTTPException, Depends
from app.models.meet_entry.meet_entry_info import MeetEntry, MeetEntryCreate, MeetEntryResponse, MeetEntryUpdate, MeetEntryJudgeView
from app.sql_lite_db.dbsql import Session, get_db

# Create the router
meet_entry_router = APIRouter(prefix="/meet-entry", tags=["Meet Entry"])

# Get all meet_entry
@meet_entry_router.get("/all", response_model=list[MeetEntryResponse])
def get_meet_entry(db: Session = Depends(get_db)):
    return db.query(MeetEntry).all()

# Get meet entry by ID
@meet_entry_router.get("/{meet_entry_id}", response_model=MeetEntryResponse)
def get_meet_entry_by_id(meet_entry_id: int, db: Session = Depends(get_db)):
    meet_entry_info = db.query(MeetEntry).filter(MeetEntry.meet_entry_id == meet_entry_id).first()
    if not meet_entry_info:
        raise HTTPException(status_code=404, detail="Meet Entry not found")
    return meet_entry_info

# Create meet entry 
@meet_entry_router.post("/create", response_model=MeetEntryCreate)
def create_meet_entry(create_meet_entry: MeetEntryCreate, db: Session = Depends(get_db)):
    
    if db.query(MeetEntry).filter(MeetEntry.gymnast_id == create_meet_entry.gymnast_id).first():
        raise HTTPException(status_code=404, detail="Meet Entry has already been done.")

    # Create new meet entry
    new_meet_entry = MeetEntry(**create_meet_entry.model_dump())
    db.add(new_meet_entry)
    db.commit()
    db.refresh(new_meet_entry)
    return new_meet_entry

# Update meet entry details by meet_entry_ID
@meet_entry_router.put("/update/{meet_entry_id}", response_model=MeetEntryResponse)
def update_meet_entry_by_id(
    meet_entry_id: int, 
    update_meet_entry: MeetEntryUpdate, 
    db: Session = Depends(get_db)):

    meet_entry_data = db.query(MeetEntry).filter(MeetEntry.meet_entry_id == meet_entry_id).first()
    if not meet_entry_data:
        raise HTTPException(status_code=404, detail="Meet Entry does not exist")
    

    data = update_meet_entry.model_dump(exclude_unset=True)


    for field, value in data.items():
        setattr(update_meet_entry, field, value)
    
    db.commit()
    db.refresh(update_meet_entry)
    return update_meet_entry

# Delete meet entry by meet_entry_ID
@meet_entry_router.delete("/delete/{meet_entry_id}")
def delete_meet_entry_by_id(meet_entry_id: int, db: Session = Depends(get_db)):
    delete_meet_entry = db.query(MeetEntry).filter(MeetEntry.meet_entry_id == meet_entry_id).first()
    if not delete_meet_entry:
        raise HTTPException(status_code=404, detail="Meet Entry does not exist")
    db.delete(delete_meet_entry)
    db.commit()
    return delete_meet_entry, {"detail": "Meet Entry deleted!"}