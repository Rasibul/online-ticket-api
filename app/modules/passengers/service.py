from fastapi import HTTPException, status

from .repository import (
    create_passenger,
    get_passengers_by_user,
    get_passenger_by_id,
    update_passenger,
    delete_passenger,
)


def serialize_passenger(
    passenger: dict
):

    return {
        "id": str(passenger["_id"]),
        "full_name": passenger["full_name"],
        "date_of_birth": passenger.get(
            "date_of_birth"
        ),
        "gender": passenger.get(
            "gender"
        ),
        "nationality": passenger.get(
            "nationality"
        ),
        "nid_or_passport": passenger.get(
            "nid_or_passport"
        ),
        "phone": passenger.get(
            "phone"
        ),
        "passenger_type": passenger[
            "passenger_type"
        ],
        "created_at": passenger[
            "created_at"
        ].isoformat(),
        "updated_at": passenger[
            "updated_at"
        ].isoformat(),
    }


async def create_user_passenger(
    user_id: str,
    passenger_data: dict
):

    passenger = await create_passenger(
        user_id,
        passenger_data
    )

    return serialize_passenger(
        passenger
    )


async def get_user_passengers(
    user_id: str
):

    passengers = await get_passengers_by_user(
        user_id
    )

    return [
        serialize_passenger(passenger)
        for passenger in passengers
    ]


async def get_user_passenger(
    user_id: str,
    passenger_id: str
):

    passenger = await get_passenger_by_id(
        user_id,
        passenger_id
    )

    if not passenger:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Passenger not found"
        )

    return serialize_passenger(
        passenger
    )


async def update_user_passenger(
    user_id: str,
    passenger_id: str,
    update_data: dict
):

    update_data = {
        key: value
        for key, value in update_data.items()
        if value is not None
    }

    if not update_data:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No passenger data provided"
        )

    passenger = await update_passenger(
        user_id,
        passenger_id,
        update_data
    )

    if not passenger:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Passenger not found"
        )

    return serialize_passenger(
        passenger
    )


async def delete_user_passenger(
    user_id: str,
    passenger_id: str
):

    result = await delete_passenger(
        user_id,
        passenger_id
    )

    if result.deleted_count == 0:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Passenger not found"
        )

    return {
        "message": "Passenger deleted successfully"
    }