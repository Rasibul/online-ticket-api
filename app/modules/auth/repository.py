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