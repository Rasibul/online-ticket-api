from app.core.database import get_database

from bson import ObjectId


async def get_user_by_id(
    user_id: str
):
    db = get_database()

    user = await db.users.find_one(
        {
            "_id": ObjectId(user_id)
        }
    )

    if not user:
        return None

    return user