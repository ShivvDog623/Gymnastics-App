from fastapi import APIRouter, HTTPException, Depends
from app.models.events.events_info import Events, EventCreate, EventUpdate, EventResponse
from app.sql_lite_db.dbsql import Session, get_db

# Create the router
events_router = APIRouter(prefix="/events", tags=["Events"])

# Get all events
@events_router.get("/all", response_model=list[EventResponse])
def get_all_events(db: Session = Depends(get_db)):
    return db.query(Events).all()

# Get event by ID
@events_router.get("/{event_id}", response_model=EventResponse)
def get_event_by_id(event_id: int, db: Session = Depends(get_db)):
    event_info = db.query(Events).filter(Events.event_id == event_id).first()
    if not event_info:
        raise HTTPException(status_code=404, detail="Event not found")
    return event_info

# Create new event
@events_router.post("/create", response_model=EventCreate)
def create_event(create_event: EventCreate, db: Session = Depends(get_db)):
    
    # Checks to see if the event already exists
    existing_event = (
        db.query(Events)
        .filter(
            Events.event_name == create_event.event_name,
            Events.gender == create_event.gender
        )
        .first()
    )
    
    if existing_event:
        raise HTTPException(status_code=400, detail="Events already exists")
    
    # Create new event
    new_event = Events(**create_event.model_dump())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

# Update event details by id
@events_router.put("/update/{event_id}", response_model=EventResponse)
def update_event_by_id(
    event_id: int, 
    update_event: EventUpdate, 
    db: Session = Depends(get_db)):

    event_data = db.query(Events).filter(Events.event_id == event_id).first()
    if not event_data:
        raise HTTPException(status_code=404, detail="Event does not exist")
    

    data = update_event.model_dump(exclude_unset=True)


    for field, value in data.items():
        setattr(event_data, field, value)
    
    db.commit()
    db.refresh(event_data)
    return event_data

# Delete event by event ID
@events_router.delete("/delete/{event_id}")
def delete_event_by_number(event_id: int, db: Session = Depends(get_db)):
    delete_event = db.query(Events).filter(Events.event_id == event_id).first()
    if not delete_event:
        raise HTTPException(status_code=404, detail="Event does not exist")
    db.delete(delete_event)
    db.commit()
    return delete_event, {"detail": "Event deleted!"}