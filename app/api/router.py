from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.modules.auth.router import router as auth_router
from app.modules.users.router import router as users_router
from app.modules.passengers.router import router as passengers_router

api_router = APIRouter()

api_router.include_router(health_router)

api_router.include_router(auth_router)

api_router.include_router(users_router)


api_router.include_router(passengers_router)
