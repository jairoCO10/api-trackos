from fastapi import APIRouter
from .auth import router as auth_router
from .organization import router as org_router
from .project import router as project_router

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(org_router)
api_router.include_router(project_router)
