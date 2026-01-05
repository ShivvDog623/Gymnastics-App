from fastapi import FastAPI
from app.sql_lite_db import dbsql

from app.models.gymnast import gymnast_details
from app.models.meet_info import meet_info 
from app.models.director import director_details
from app.models.coaches import coaches_details
from app.models.judges import judges_info
from app.models.events import events_info 
from app.models.gyms import gyms_info
from app.models.gym_coaches import gym_coaches_info
from app.models.teams import teams_info
from app.models.scores import scores_info
from app.models.session import session
from app.models.meet_entry import meet_entry_info

dbsql.Base.metadata.create_all(bind=dbsql.engine)


def register_routers(app):
    from app.routers.health.health_router import health_router
    from app.routers.meet_info.meet_info_blueprint import meet_details_router
    from app.routers.gymnast.gymnast_blueprint import gymnast_router
    from app.routers.director.director_blueprint import director_router
    from app.routers.coaches.coaches_blueprint import coach_router
    from app.routers.judges.judges_blueprint import judge_router
    from app.routers.events.events_blueprint import events_router
    from app.routers.gyms.gyms_blueprint import gyms_router
    from app.routers.gyms_coaches.gyms_coaches_blueprint import gym_coaches_router
    from app.routers.teams.teams_blueprint import teams_router
    from app.routers.scores.scores_blueprint import scores_router
    from app.routers.meet_entry.meet_entry_blueprint import meet_entry_router
    from app.routers.session.session_blueprint import session_router

    # Include the routers
    app.include_router(health_router)
    app.include_router(meet_details_router)
    app.include_router(gymnast_router)
    app.include_router(director_router)
    app.include_router(coach_router)
    app.include_router(judge_router)
    app.include_router(events_router)
    app.include_router(gyms_router)
    app.include_router(gym_coaches_router)
    app.include_router(teams_router)
    app.include_router(scores_router)
    app.include_router(meet_entry_router)
    app.include_router(session_router)



def create_app():
    app = FastAPI(title="Gymnastics App API", version="1.0.0")

    dbsql.get_db()

    register_routers(app)
    return app
