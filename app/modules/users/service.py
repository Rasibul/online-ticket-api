from fastapi import HTTPException,status

from .repository import get_user_by_id



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