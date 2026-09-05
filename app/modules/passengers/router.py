from fastapi import APIRouter, Depends, status

from app.core.dependencies import (
    get_current_user_id
)

from .schema import (
    PassengerCreateRequest,
    PassengerUpdateRequest,
    PassengerResponse,
)

from .service import (
    create_user_passenger,
    get_user_passengers,
    get_user_passenger,
    update_user_passenger,
    delete_user_passenger,
)


router = APIRouter(
    prefix="/passengers",
    tags=["Passengers"]
)


@router.post(
    "",
    response_model=PassengerResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_passenger_endpoint(

    payload: PassengerCreateRequest,

    user_id: str = Depends(
        get_current_user_id
    )

):

    return await create_user_passenger(
        user_id=user_id,
        passenger_data=payload.model_dump()
    )


@router.get(
    "",
    response_model=list[PassengerResponse]
)
async def get_passengers_endpoint(

    user_id: str = Depends(
        get_current_user_id
    )

):

    return await get_user_passengers(
        user_id
    )


@router.get(
    "/{passenger_id}",
    response_model=PassengerResponse
)
async def get_passenger_endpoint(

    passenger_id: str,

    user_id: str = Depends(
        get_current_user_id
    )

):

    return await get_user_passenger(
        user_id,
        passenger_id
    )


@router.put(
    "/{passenger_id}",
    response_model=PassengerResponse
)
async def update_passenger_endpoint(

    passenger_id: str,

    payload: PassengerUpdateRequest,

    user_id: str = Depends(
        get_current_user_id
    )

):

    return await update_user_passenger(
        user_id=user_id,
        passenger_id=passenger_id,
        update_data=payload.model_dump(
            exclude_unset=True
        )
    )


@router.delete(
    "/{passenger_id}"
)
async def delete_passenger_endpoint(

    passenger_id: str,

    user_id: str = Depends(
        get_current_user_id
    )

):

    return await delete_user_passenger(
        user_id,
        passenger_id
    )