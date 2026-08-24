from fastapi import HTTPException
import jwt
from app.modules.auth.models import UserModel
from app.modules.auth.schemas import RegisterRequest
from app.modules.notifications.email_service import send_email
from app.modules.notifications.email_templates import verification_email_template
from datetime import datetime, timezone



from app.modules.auth.repository import (
    find_user_by_id,
    find_user_by_email,
    find_user_by_username,
    find_user_by_phone,
    create_user,
    find_user_by_verification_token,
    verify_user,
    update_refresh_token
)
from app.core.security import (
    hash_password,
    generate_verification_token,
    get_token_expiry,
    verify_password,
    create_access_token,
    create_refresh_token
)
from app.core.config import settings
















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


    verification_token = generate_verification_token(
        payload.email
    )

    verification_token_expiry = get_token_expiry()



    user_data = UserModel.create_document(

    username=payload.username,

    email=payload.email,

    phone=payload.phone,

    password_hash=password_hash,

    verification_token=
        verification_token,

    verification_token_expiry=
        verification_token_expiry

)


    user_id = await create_user(
        user_data
    )

    await send_email(

    to_email=payload.email,

    subject="Verify Your Email",

    html_content=
    verification_email_template(
        verification_token
    )

)

    await send_email(
    to_email=payload.email,
    subject="Registration Successful",
    html_content="""
        <h2>Welcome!</h2>
        <p>Your account has been created successfully.</p>
    """
)


    return str(user_id)






async def verify_email(token:str):


    user = await find_user_by_verification_token(
        token
    )


    if not user:

        raise HTTPException(
            status_code=400,
            detail="Invalid verification token"
        )


    expiry = (
        user["verification_token_expiry"]
    )


    if expiry < datetime.now(timezone.utc):

        raise HTTPException(
            status_code=400,
            detail="Verification token expired"
        )


    await verify_user(
        user["_id"]
    )


    return True





async def login_user(payload):


    user = await find_user_by_email(
        payload.email
    )


    if not user:

        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )


    password_valid = verify_password(

        payload.password,

        user["password"]

    )


    if not password_valid:

        raise HTTPException(
            status_code=400,
            detail="Invalid credentials"
        )


    if not user["is_verified"]:

        raise HTTPException(

            status_code=403,

            detail="Email not verified"

        )


    token_payload = {

        "user_id":
        str(user["_id"]),

        "role":
        user["role"]

    }


    access_token = (
        create_access_token(
            token_payload
        )
    )


    refresh_token = (
        create_refresh_token(
            token_payload
        )
    )


    await update_refresh_token(

        user["_id"],

        refresh_token

    )


    return {

        "access_token":
        access_token,


        "refresh_token":
        refresh_token,


        "token_type":
        "bearer",


        "role":
        user["role"]

    }


async def get_current_user(token:str):


    try:

        payload = jwt.decode(

            token,

            settings.jwt_secret,

            algorithms=[

                settings.jwt_algorithm

            ]

        )


        user_id = payload.get("user_id")


        if not user_id:

            raise HTTPException(

                status_code=401,

                detail="Invalid token"

            )


        user = await find_user_by_id(
            user_id
        )


        if not user:

            raise HTTPException(

                status_code=401,

                detail="User not found"

            )


        return user


    except jwt.ExpiredSignatureError:

        raise HTTPException(

            status_code=401,

            detail="Token has expired"

        )


    except jwt.InvalidTokenError:

        raise HTTPException(

            status_code=401,

            detail="Invalid token"

        )