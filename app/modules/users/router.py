from fastapi import APIRouter, Depends

from app.core.dependencies import get_current_user_id

from .schema import (
    UpdateProfileRequest,
    UserProfileResponse,
    ChangePasswordRequest
)

from .service import (
    update_current_user_profile,
     change_current_user_password
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.put(
    "/profile",
    response_model=UserProfileResponse
)
async def update_profile(

    payload: UpdateProfileRequest,

    user_id: str = Depends(
        get_current_user_id
    )

):

    return await update_current_user_profile(
        user_id=user_id,
        update_data=payload.model_dump(
            exclude_unset=True
        )
    )



@router.put(
    "/change-password"
)
async def change_password(

    payload: ChangePasswordRequest,

    user_id: str = Depends(
        get_current_user_id
    )

):

    return await change_current_user_password(

        user_id=user_id,

        current_password=payload.current_password,

        new_password=payload.new_password

    )