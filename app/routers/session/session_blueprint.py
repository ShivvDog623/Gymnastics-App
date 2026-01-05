from fastapi import APIRouter, HTTPException, Depends
from app.models.session.session import Sessions, SessionCreate, SessionUpdate, SessionResponse
from app.sql_lite_db.dbsql import Session, get_db

# Create the router
session_router = APIRouter(prefix="/session", tags=["Session"])

# Get all sessions
@session_router.get("/all", response_model=list[SessionResponse])
def get_all_sessions(db: Session = Depends(get_db)):
    return db.query(Sessions).all()

# Get session by ID
@session_router.get("/{session_id}", response_model=SessionResponse)
def get_session_by_id(session_id: int, db: Session = Depends(get_db)):
    session_info = db.query(Sessions).filter(Sessions.session_id == session_id).first()
    if not session_info:
        raise HTTPException(status_code=404, detail="Session not found")
    return session_info

# Create new session
@session_router.post("/create", response_model=SessionResponse)
def create_session(create_session: SessionCreate, db: Session = Depends(get_db)):

    if db.query(Sessions).filter(Sessions.session_number == create_session.session_number).first():
        raise HTTPException(status_code=400, detail="Session already exists")
    
    # Create new session
    new_session = Sessions(**create_session.model_dump())
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

# Update session details by id
@session_router.put("/update/{session_id}", response_model=SessionResponse)
def update_session_by_id(
    session_id: int, 
    update_session: SessionUpdate, 
    db: Session = Depends(get_db)):

    session_data = db.query(Sessions).filter(Sessions.session_id == session_id).first()
    if not session_data:
        raise HTTPException(status_code=404, detail="Session does not exist")
    

    data = update_session.model_dump(exclude_unset=True)


    for field, value in data.items():
        setattr(session_data, field, value)
    
    db.commit()
    db.refresh(session_data)
    return session_data

# Delete session by ID
@session_router.delete("/delete/{session_id}")
def delete_session_id(session_id: int, db: Session = Depends(get_db)):
    delete_session = db.query(Sessions).filter(Sessions.session_id == session_id).first()
    if not delete_session:
        raise HTTPException(status_code=404, detail="Session does not exist")
    db.delete(delete_session)
    db.commit()
    return delete_session, {"detail": "Session deleted!"}