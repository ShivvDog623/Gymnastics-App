from fastapi import APIRouter, HTTPException, Depends
from app.models.judges.judges_info import Judges, JudgeCreate, JudgeResponse, JudgeUpdate
from app.sql_lite_db.dbsql import Session, get_db

# Create the router
judge_router = APIRouter(prefix="/judges", tags=["Judges"])

# Get all judges
@judge_router.get("/all", response_model=list[JudgeResponse])
def get_all_judges(db: Session = Depends(get_db)):
    return db.query(Judges).all()

# Create a new judge
@judge_router.post("/create", response_model=JudgeCreate)
def create_judge(judge_data: JudgeCreate, db: Session = Depends(get_db)):
    if db.query(Judges).filter(Judges.judge_pro_number == judge_data.judge_pro_number).first():
        raise HTTPException(status_code=409, detail="Judge with this pro number already exists")
    
    new_judge = Judges(**judge_data.model_dump())
    db.add(new_judge)
    db.commit()
    db.refresh(new_judge)
    return new_judge

# Get judges by ID
@judge_router.get("/{judge_id}", response_model=JudgeResponse)
def get_judge_by_id(judge_id: int, db: Session = Depends(get_db)):
    judge_info = db.query(Judges).filter(Judges.judge_id == judge_id).first()
    if not judge_info:
        raise HTTPException(status_code=404, detail="Judge not found")
    return judge_info

# Get judge by USAG Pro Number
@judge_router.get("/pro-number/{judge_pro_number}", response_model=JudgeResponse)
def get_judge_by_pro_number(judge_pro_number: int, db: Session = Depends(get_db)):
    judge_info = db.query(Judges).filter(Judges.judge_pro_number == judge_pro_number).first()
    if not judge_info:
        raise HTTPException(status_code=404, detail="Judge not found")
    return judge_info

# Update judge details by judge_id
@judge_router.put("/update/{judge_pro_number}", response_model=JudgeResponse)
def update_judge_by_id(
    judge_pro_number: int, 
    update_judge: JudgeUpdate,
    db: Session = Depends(get_db)):

    judge_data = db.query(Judges).filter(Judges.judge_pro_number == judge_pro_number).first()
    if not judge_data:
        raise HTTPException(status_code=404, detail="Judge does not exist")
    

    data = update_judge.model_dump(exclude_unset=True)


    for field, value in data.items():
        setattr(judge_data, field, value)
    
    db.commit()
    db.refresh(judge_data)
    return judge_data

# Delete judge by judge by pro number
@judge_router.delete("/delete/{judge_pro_number}")
def delete_judge_by_pro_number(judge_pro_number: int, db: Session = Depends(get_db)):
    delete_judge = db.query(Judges).filter(Judges.judge_pro_number == judge_pro_number).first()
    if not delete_judge:
        raise HTTPException(status_code=404, detail="Judge does not exist")
    db.delete(delete_judge)
    db.commit()
    return delete_judge, {"detail": "Judge deleted!"}