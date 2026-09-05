from pydantic import BaseModel, Field, ConfigDict


class UpdateProfileRequest(BaseModel):

    username: str | None = Field(
        default=None,
        min_length=3,
        max_length=50
    )

    phone: str | None = Field(
        default=None,
        min_length=7,
        max_length=20
    )


class UserProfileResponse(BaseModel):

    model_config = ConfigDict(
        populate_by_name=True
    )

    id: str
    username: str
    email: str
    phone: str
    role: str
    is_verified: bool
    is_active: bool




class ChangePasswordRequest(BaseModel):

    current_password: str = Field(
        min_length=1
    )

    new_password: str = Field(
        min_length=8,
        max_length=128
    )    