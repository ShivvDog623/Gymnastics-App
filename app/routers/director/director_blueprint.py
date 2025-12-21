from fastapi import APIRouter, HTTPException, Depends
from app.models.director.director_details import Director, DirectorCreate, DirectorUpdate, DirectorResponse 
from app.sql_lite_db.dbsql import Session, get_db


# Create the router
director_router = APIRouter(prefix="/directors", tags=["Directors"])

# Get all directors
@director_router.get("/all", response_model=list[DirectorResponse])
def get_all_directors(db: Session = Depends(get_db)):
    return db.query(Director).all()

# Get director by ID
@director_router.get("/{director_id}", response_model=DirectorResponse)
def get_director_by_id(director_id: int, db: Session = Depends(get_db)):
    directors = db.query(Director).filter(Director.director_id == director_id).first()
    if not directors:
        raise HTTPException(status_code=404, detail="Director details not found")
    return directors

# Create new director 
@director_router.post("/create", response_model=DirectorCreate)
def create_director(create_director: DirectorCreate, db: Session = Depends(get_db)):
    if db.query(Director).filter(Director.email == create_director.email).first():
        raise HTTPException(status_code=404, detail="Email is already used")
    
    # Creates director
    new_director = Director(**create_director.model_dump())
    db.add(new_director)
    db.commit()
    db.refresh(new_director)
    return new_director

@director_router.put("/update/{director_id}", response_model=DirectorResponse)
def update_director(director_id: int, update_director: DirectorUpdate, db: Session = Depends(get_db)):
    
    director = db.query(Director).filter(Director.director_id == director_id).first()

    if not director:
        raise HTTPException(status_code=404, detail="Director does not exist")

    data = update_director.model_dump(exclude_unset=True)

    for field, value in data.items():
        setattr(director, field, value)

    db.commit()
    db.refresh(director)
    return director

@director_router.delete("/delete/{director_id}")
def delete_director(director_id: int, db: Session = Depends(get_db)):
    director_delete = db.query(Director).filter(Director.director_id == director_id).first()

    if not director_delete:
        raise HTTPException(status_code=404, detail="Director does not exist")
    
    db.delete(director_delete)
    db.commit()
    return director_delete, {"detail": "Director deleted!"}