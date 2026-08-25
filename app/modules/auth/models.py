from datetime import datetime, timezone


class UserModel:


    @staticmethod
    def create_document(
        username: str,
        email: str,
        phone: str,
        password_hash: str,
        verification_token: str,
        verification_token_expiry,
        role="USER",
    ):


        return {

            "username": username,

            "email": email.lower(),

            "phone": phone,

            "password": password_hash,


            "role": role,


            "is_verified": False,


            "verification_token": verification_token,


            "verification_token_expiry":verification_token_expiry,
            "refresh_token": None,
            "refresh_token_created_at": None,
            "last_login_at": None,

            "is_active": True,


            "created_at": datetime.now(timezone.utc),


            "updated_at":datetime.now(timezone.utc)

        }