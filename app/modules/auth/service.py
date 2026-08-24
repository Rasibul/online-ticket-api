from fastapi import HTTPException, status

from app.modules.auth.repository import (
    find_user_by_email,
    find_user_by_username,
    find_user_by_phone,
    create_user,
)

from app.modules.auth.models import UserModel
from app.modules.auth.schemas import RegisterRequest
from app.core.security import hash_password



async def register_user(
    payload:RegisterRequest
):

    existing_email = await find_user_by_email(
        payload.email
    )

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )


    existing_username = await find_user_by_username(
        payload.username
    )


    if existing_username:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )


    existing_phone = await find_user_by_phone(
        payload.phone
    )


    if existing_phone:
        raise HTTPException(
            status_code=400,
            detail="Phone already exists"
        )


    password_hash = hash_password(
        payload.password
    )


    user_data = UserModel.create_document(
        username=payload.username,
        email=payload.email,
        phone=payload.phone,
        password_hash=password_hash
    )


    user_id = await create_user(
        user_data
    )


    return str(user_id)