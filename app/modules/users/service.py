from fastapi import HTTPException,status

from .repository import get_user_by_id

from fastapi import HTTPException, status

from .repository import (
    get_user_by_id,
    update_user_profile,
    find_user_by_username,
    update_user_password
)



from app.core.security import (
    verify_password,
    hash_password
)


async def get_current_user(
    user_id:str
):


    user = await get_user_by_id(
        user_id
    )


    if not user:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )


    return {

        "id":str(user["_id"]),

        "username":user["username"],

        "email":user["email"],

        "phone":user["phone"],

        "role":user["role"],

        "is_verified":user["is_verified"],

        "is_active":user["is_active"]

    }


async def update_current_user_profile(
    user_id: str,
    update_data: dict
):

    user = await get_user_by_id(
        user_id
    )

    if not user:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )


    update_data = {
        key: value.strip() if isinstance(value, str) else value
        for key, value in update_data.items()
        if value is not None
    }


    if not update_data:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No profile data provided"
        )


    # Check username uniqueness
    if "username" in update_data:

        new_username = update_data["username"]

        if new_username.lower() != user["username"].lower():

            existing_user = await find_user_by_username(
                new_username
            )

            if existing_user:

                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Username already exists"
                )


    await update_user_profile(
        user_id,
        update_data
    )


    updated_user = await get_user_by_id(
        user_id
    )


    return {
        "id": str(updated_user["_id"]),
        "username": updated_user["username"],
        "email": updated_user["email"],
        "phone": updated_user["phone"],
        "role": updated_user["role"],
        "is_verified": updated_user["is_verified"],
        "is_active": updated_user["is_active"]
    }




async def change_current_user_password(
    user_id: str,
    current_password: str,
    new_password: str
):

    user = await get_user_by_id(
        user_id
    )


    if not user:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )


    # Verify current password

    password_is_valid = verify_password(

        current_password,

        user["password"]

    )


    if not password_is_valid:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect"
        )


    # Prevent using the same password

    if verify_password(
        new_password,
        user["password"]
    ):

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New password must be different from current password"
        )


    # Hash new password

    hashed_password = hash_password(
        new_password
    )


    # Update password and invalidate session

    await update_user_password(

        user_id,

        hashed_password

    )


    return {
        "message": "Password changed successfully"
    }