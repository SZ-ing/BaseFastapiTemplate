from fastapi import APIRouter
from .endpoints import base_api

api_router = APIRouter()
api_router.include_router(base_api.router, prefix="/api/default", tags=["default"])

