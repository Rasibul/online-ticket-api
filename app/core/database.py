from pymongo import AsyncMongoClient

from app.core.config import settings


client: AsyncMongoClient | None = None
database = None


async def connect_to_mongodb() -> None:
    global client, database

    client = AsyncMongoClient(settings.mongodb_uri)

    await client.admin.command("ping")

    database = client[settings.mongodb_db_name]


async def close_mongodb() -> None:
    global client

    if client is not None:
        await client.close()


def get_database():
    if database is None:
        raise RuntimeError("MongoDB is not initialized.")

    return database