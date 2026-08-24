from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):

    username: str = Field(
        min_length=3,
        max_length=30
    )

    email: EmailStr

    phone: str = Field(
        min_length=10,
        max_length=15
    )

    password: str = Field(
        min_length=8
    )


class RegisterResponse(BaseModel):

    message: str
    user_id: str


class LoginRequest(BaseModel):

    email: EmailStr

    password: str



class LoginResponse(BaseModel):

    access_token:str

    refresh_token:str

    token_type:str

    role:str