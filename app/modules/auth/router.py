from fastapi import APIRouter,Body, Depends
from fastapi import Query
from app.modules.auth.schemas import (
    RegisterRequest,
    RegisterResponse
)
from app.modules.auth.schemas import (
    LoginRequest,
    LoginResponse
)
from app.modules.auth.service import get_current_user, get_current_user, login_user, logout_user, logout_user, refresh_access_token, register_user, verify_email
from app.core.dependencies import get_current_user_id
from app.modules.users.service import get_current_user


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


@router.post(
    "/login",
    response_model=LoginResponse
)
async def login(
    payload:LoginRequest
):

    return await login_user(
        payload
    )


@router.post(
    "/refresh"
)
async def refresh_token(

    refresh_token:str = Body(...)

):


    return await refresh_access_token(

        refresh_token

    )



@router.post(
    "/logout"
)
async def logout(

    user=Depends(
        get_current_user
    )

):


    await logout_user(

        user["user_id"]

    )


    return {

        "message":
        "Logout successful"

    }



@router.get(
    "/me"
)
async def current_user(

    user_id:str = Depends(
        get_current_user_id
    )

):


    user = await get_current_user(
        user_id
    )


    return {

        "success":True,

        "data":user

    }