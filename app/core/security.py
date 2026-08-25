import bcrypt
import secrets
from datetime import datetime, timedelta, timezone
import jwt
from app.core.config import settings
from fastapi import HTTPException

def hash_password(password: str) -> str:

    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(
        password.encode(),
        salt
    )

    return hashed.decode()



def verify_password(
    password: str,
    hashed_password: str
) -> bool:

    return bcrypt.checkpw(
        password.encode(),
        hashed_password.encode()
    )




def generate_verification_token():

    return secrets.token_urlsafe(32)





def get_token_expiry():

    return (
        datetime.now(timezone.utc)
        +
        timedelta(hours=24)
    )







def create_access_token(
    data: dict
):

    payload = data.copy()


    expire = (
        datetime.now(timezone.utc)
        +
        timedelta(
            minutes=
            settings.access_token_expire_minutes
        )
    )


    payload.update(
        {
            "exp": expire,
            "type": "access"
        }
    )


    token = jwt.encode(
        payload,
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm
    )


    return token


def create_refresh_token(
    data:dict
):

    payload=data.copy()


    expire = (
        datetime.now(timezone.utc)
        +
        timedelta(
            days=
            settings.refresh_token_expire_days
        )
    )


    payload.update(
        {
            "exp":expire,

            "type":"refresh"
        }
    )


    return jwt.encode(
        payload,

        settings.jwt_secret,

        algorithm=settings.jwt_algorithm
    )





def decode_token(token:str):

    try:

        payload = jwt.decode(
            token,
            settings.jwt_secret,
            algorithms=[
                settings.jwt_algorithm
            ]
        )

        return payload


    except jwt.ExpiredSignatureError:

        raise HTTPException(
            status_code=401,
            detail="Token expired"
        )


    except jwt.InvalidTokenError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )