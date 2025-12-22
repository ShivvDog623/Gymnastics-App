from fastapi import APIRouter, HTTPException, Depends
from app.models.teams.teams_info import Teams, TeamUpdate, TeamCreate, TeamResponse
from app.sql_lite_db.dbsql import Session, get_db

# Create the router
teams_router = APIRouter(prefix="/teams", tags=["Teams"])

# Get all teams
@teams_router.get("/all", response_model=list[TeamResponse])
def get_all_teams(db: Session = Depends(get_db)):
    return db.query(Teams).all()

# Get team by ID
@teams_router.get("/{team_id}", response_model=TeamResponse)
def get_team_by_id(team_id: int, db: Session = Depends(get_db)):
    team_info = db.query(Teams).filter(Teams.team_id == team_id).first()
    if not team_info:
        raise HTTPException(status_code=404, detail="Team not found")
    return team_info

# Create new team
@teams_router.post("/create", response_model=TeamCreate)
def create_team(create_team: TeamCreate, db: Session = Depends(get_db)):
    
    # Checks to see if the team already exists
    existing_team = (
        db.query(Teams)
        .filter(
            Teams.level == create_team.level,
            Teams.division == create_team.division,
            Teams.external_team_id == create_team.external_team_id,
            Teams.gym_id == create_team.gym_id
        )
        .first()
    )
    
    if existing_team:
        raise HTTPException(status_code=400, detail="Team already exists")
    
    # Create new team
    new_team = Teams(**create_team.model_dump())
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team

# Update team details by id
@teams_router.put("/update/{team_id}", response_model=TeamResponse)
def update_team_by_id(
    team_id: int, 
    update_team: TeamUpdate, 
    db: Session = Depends(get_db)):

    team_data = db.query(Teams).filter(Teams.team_id == team_id).first()
    if not team_data:
        raise HTTPException(status_code=404, detail="Team does not exist")
    

    data = update_team.model_dump(exclude_unset=True)


    for field, value in data.items():
        setattr(team_data, field, value)
    
    db.commit()
    db.refresh(team_data)
    return team_data

# Delete team by ID
@teams_router.delete("/delete/{team_id}")
def delete_team_by_id(team_id: int, db: Session = Depends(get_db)):
    delete_team = db.query(Teams).filter(Teams.team_id == team_id).first()
    if not delete_team:
        raise HTTPException(status_code=404, detail="Team does not exist")
    db.delete(delete_team)
    db.commit()
    return delete_team, {"detail": "Team deleted!"}