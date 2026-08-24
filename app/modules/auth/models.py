from datetime import datetime, timezone
from typing import Optional

from bson import ObjectId


from app.shared.enums import UserRole


class UserModel:

    collection_name = "users"

    @staticmethod
    def create_document(
        username: str,
        email: str,
        phone: str,
        password_hash: str,
        role: UserRole = UserRole.USER,
    ):

        return {
            "_id": ObjectId(),

            "username": username,
            "email": email.lower(),
            "phone": phone,

            "password": password_hash,

            "role": role.value,

            "is_verified": False,
            "is_active": True,

            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc),
        }