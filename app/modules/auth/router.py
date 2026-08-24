from fastapi import APIRouter
from fastapi import Query
from app.modules.auth.schemas import (
    RegisterRequest,
    RegisterResponse
)

from app.modules.auth.service import register_user, verify_email



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


@router.get(
    "/verify-email"
)
async def verify_email_account(
    token:str = Query(...)
):


    await verify_email(token)


    return {

        "message":
        "Email verified successfully"

    }