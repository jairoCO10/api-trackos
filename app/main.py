from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TrackOS API")
app.include_router(api_router)
