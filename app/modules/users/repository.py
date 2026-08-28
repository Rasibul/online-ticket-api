from app.core.database import get_database

from bson import ObjectId


async def get_user_by_id(user_id: str):

    db = get_database()

    user = await db.users.find_one(
        {
            "_id": ObjectId(user_id)
        }
    )

    return user


async def update_user_profile(
    user_id: str,
    update_data: dict
):

    db = get_database()

    result = await db.users.update_one(
        {
            "_id": ObjectId(user_id)
        },
        {
            "$set": update_data
        }
    )

    return result



async def find_user_by_username(
    username: str
):

    db = get_database()

    user = await db.users.find_one(
        {
            "username": username
        }
    )

    return user