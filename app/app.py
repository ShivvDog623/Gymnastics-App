from fastapi import FastAPI
from app.models.meet_details import meet_details 
from app.sql_lite_db import dbsql


meet_details.Base.metadata.create_all(bind=dbsql.engine)


def register_routers(app):
    from app.routers.health.health_router import health_router
    from app.routers.meet_details.meet_details_blueprint import meet_details_router


    # Include the routers
    app.include_router(health_router)
    app.include_router(meet_details_router)

def create_app():
    app = FastAPI(title="Gymnastics App API", version="1.0.0")

    dbsql.get_db()

    register_routers(app)
    return app
