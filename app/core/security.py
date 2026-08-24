import bcrypt
import secrets
from datetime import datetime, timedelta, timezone


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