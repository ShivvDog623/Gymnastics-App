from fastapi import APIRouter, HTTPException, Depends
from app.models.gymnast.gymnast_details import Gymnast, GymnastCreate, GymnastResponse, GymnastUpdate
from app.sql_lite_db.dbsql import Session, get_db

# Create the router
gymnast_router = APIRouter(prefix="/gymnast", tags=["Gymnast"])

# Get all gymnasts
@gymnast_router.get("/all", response_model=list[GymnastResponse])
def get_all_gymnasts(db: Session = Depends(get_db)):
    return db.query(Gymnast).all()

# Get gymnast by ID
@gymnast_router.get("/{gymnast_id}", response_model=GymnastResponse)
def get_gymnast_by_id(gymnast_id: int, db: Session = Depends(get_db)):
    gymnast_info = db.query(Gymnast).filter(Gymnast.id == gymnast_id).first()
    if not gymnast_info:
        raise HTTPException(status_code=404, detail="Gymnast not found")
    return gymnast_info

# Get gymnast by gymnast number
@gymnast_router.get("/number/{gymnast_number}", response_model=GymnastResponse)
def get_gymnast_by_number(gymnast_number: int, db: Session = Depends(get_db)):
    gymnast_info = db.query(Gymnast).filter(Gymnast.gymnast_number == gymnast_number).first()
    if not gymnast_info:
        raise HTTPException(status_code=404, detail="Gymnast not found")
    return gymnast_info

# Get gymnast by usag number
@gymnast_router.get("/usag/{usag_number}", response_model=GymnastResponse)
def get_gymnast_by_usag(usag_number: int, db: Session = Depends(get_db)):
    gymnast_info = db.query(Gymnast).filter(Gymnast.usag_number == usag_number).first()
    if not gymnast_info:
        raise HTTPException(status_code=404, detail="Gymnast not found")
    return gymnast_info

# Create new gymnast
@gymnast_router.post("/create", response_model=GymnastResponse)
def create_gymnast(create_gymnast: GymnastCreate, db: Session = Depends(get_db)):
    if db.query(Gymnast).filter(Gymnast.gymnast_number == create_gymnast.gymnast_number).first():
        raise HTTPException(status_code=400, detail="Gymnast already exists")
    
    # Create new gymnast
    new_gymnast = Gymnast(**create_gymnast.model_dump())
    db.add(new_gymnast)
    db.commit()
    db.refresh(new_gymnast)
    return new_gymnast

# Update gymnast details by gymnast number
@gymnast_router.put("/update/{gymnast_number}", response_model=GymnastResponse)
def update_gymnast_by_number(
    gymnast_number: int, 
    update_gymnast: GymnastUpdate, 
    db: Session = Depends(get_db)):

    gymnast_data = db.query(Gymnast).filter(Gymnast.gymnast_number == gymnast_number).first()
    if not gymnast_data:
        raise HTTPException(status_code=404, detail="Meet does not exist")
    

    data = update_gymnast.model_dump(exclude_unset=True)


    for field, value in data.items():
        setattr(gymnast_data, field, value)
    
    db.commit()
    db.refresh(gymnast_data)
    return gymnast_data

# Delete gymnast by gymnast number
@gymnast_router.delete("/delete/{gymnast_number}")
def delete_gymnast_by_number(gymnast_number: int, db: Session = Depends(get_db)):
    delete_gymnast = db.query(Gymnast).filter(Gymnast.gymnast_number == gymnast_number).first()
    if not delete_gymnast:
        raise HTTPException(status_code=404, detail="Gymnast does not exist")
    db.delete(delete_gymnast)
    db.commit()
    return delete_gymnast, {"detail": "Gymnast deleted!"}