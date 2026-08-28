from pydantic import BaseModel


class UserProfileResponse(BaseModel):

    id:str

    username:str

    email:str

    phone:str

    role:str

    is_verified:bool

    is_active:bool