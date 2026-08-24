from app.core.database import get_database


async def find_user_by_email(email:str):

    db = get_database()

    return await db.users.find_one(
        {
            "email": email.lower()
        }
    )



async def find_user_by_username(username:str):

    db = get_database()

    return await db.users.find_one(
        {
            "username": username
        }
    )



async def find_user_by_phone(phone:str):

    db = get_database()

    return await db.users.find_one(
        {
            "phone": phone
        }
    )



async def create_user(data:dict):

    db = get_database()

    result = await db.users.insert_one(data)

    return result.inserted_id


async def find_user_by_verification_token(
    token:str
):

    db = get_database()


    return await db.users.find_one(
        {
            "verification_token": token
        }
    )


async def verify_user(
    user_id
):

    db = get_database()


    await db.users.update_one(

        {
            "_id": user_id
        },

        {
            "$set":
            {
                "is_verified": True,

                "verification_token": None,

                "verification_token_expiry": None
            }
        }

    )