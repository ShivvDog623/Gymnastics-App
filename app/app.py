from fastapi import FastAPI
from app.sql_lite_db import dbsql

from app.models.gymnast import gymnast_details
from app.models.meet_info import meet_info 
from app.models.director import director_details
from app.models.coaches import coaches_details

dbsql.Base.metadata.create_all(bind=dbsql.engine)


def register_routers(app):
    from app.routers.health.health_router import health_router
    from app.routers.meet_info.meet_info_blueprint import meet_details_router
    from app.routers.gymnast.gymnast_blueprint import gymnast_router
    from app.routers.director.director_blueprint import director_router
    from app.routers.coaches.coaches_blueprint import coach_router

    # Include the routers
    app.include_router(health_router)
    app.include_router(meet_details_router)
    app.include_router(gymnast_router)
    app.include_router(director_router)
    app.include_router(coach_router)


def create_app():
    app = FastAPI(title="Gymnastics App API", version="1.0.0")

    dbsql.get_db()

    register_routers(app)
    return app
