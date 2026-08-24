from fastapi import APIRouter

from app.modules.auth.schemas import (
    RegisterRequest,
    RegisterResponse
)

from app.modules.auth.service import register_user



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)



@router.post(
    "/register",
    response_model=RegisterResponse
)
async def register(
    payload:RegisterRequest
):

    user_id = await register_user(
        payload
    )


    return {
        "message": "Registration successful",
        "user_id": user_id
    }