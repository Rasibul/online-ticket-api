from datetime import datetime, timezone

from bson import ObjectId

from app.core.database import get_database

async def create_passenger(
    user_id: str,
    passenger_data: dict
):

    db = get_database()

    now = datetime.now(timezone.utc)

    document = {
        "user_id": ObjectId(user_id),
        **passenger_data,
        "created_at": now,
        "updated_at": now,
    }

    result = await db.passengers.insert_one(
        document
    )

    return await db.passengers.find_one(
        {
            "_id": result.inserted_id
        }
    )


async def get_passengers_by_user(
    user_id: str
):

    db = get_database()

    cursor = db.passengers.find(
        {
            "user_id": ObjectId(user_id)
        }
    ).sort(
        "created_at",
        -1
    )

    return await cursor.to_list(
        length=None
    )


async def get_passenger_by_id(
    user_id: str,
    passenger_id: str
):

    db = get_database()

    return await db.passengers.find_one(
        {
            "_id": ObjectId(passenger_id),
            "user_id": ObjectId(user_id)
        }
    )


async def update_passenger(
    user_id: str,
    passenger_id: str,
    update_data: dict
):

    db = get_database()

    update_data["updated_at"] = (
        datetime.now(timezone.utc)
    )

    await db.passengers.update_one(
        {
            "_id": ObjectId(passenger_id),
            "user_id": ObjectId(user_id)
        },
        {
            "$set": update_data
        }
    )

    return await get_passenger_by_id(
        user_id,
        passenger_id
    )


async def delete_passenger(
    user_id: str,
    passenger_id: str
):

    db = get_database()

    result = await db.passengers.delete_one(
        {
            "_id": ObjectId(passenger_id),
            "user_id": ObjectId(user_id)
        }
    )

    return result