from pymongo import AsyncMongoClient

from app.core.config import settings


client: AsyncMongoClient | None = None
database = None


async def connect_to_mongodb() -> None:
    global client, database

    client = AsyncMongoClient(settings.database_uri)

    await client.admin.command("ping")

    database = client[settings.database_name]


async def close_mongodb() -> None:
    global client

    if client is not None:
        await client.close()


def get_database():
    if database is None:
        raise RuntimeError("MongoDB is not initialized.")

    return database


async def create_indexes():

    db = get_database()


    await db.users.create_index(
        "email",
        unique=True
    )


    await db.users.create_index(
        "username",
        unique=True
    )


    await db.users.create_index(
        "phone",
        unique=True
    )