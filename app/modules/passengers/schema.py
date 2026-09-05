from datetime import date

from pydantic import BaseModel, Field


class PassengerCreateRequest(BaseModel):

    full_name: str = Field(
        min_length=2,
        max_length=100
    )

    date_of_birth: date | None = None

    gender: str | None = Field(
        default=None,
        max_length=20
    )

    nationality: str | None = Field(
        default=None,
        max_length=50
    )

    nid_or_passport: str | None = Field(
        default=None,
        max_length=50
    )

    phone: str | None = Field(
        default=None,
        max_length=20
    )

    passenger_type: str = Field(
        default="ADULT",
        max_length=20
    )


class PassengerUpdateRequest(BaseModel):

    full_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    date_of_birth: date | None = None

    gender: str | None = Field(
        default=None,
        max_length=20
    )

    nationality: str | None = Field(
        default=None,
        max_length=50
    )

    nid_or_passport: str | None = Field(
        default=None,
        max_length=50
    )

    phone: str | None = Field(
        default=None,
        max_length=20
    )

    passenger_type: str | None = Field(
        default=None,
        max_length=20
    )


class PassengerResponse(BaseModel):

    id: str

    full_name: str

    date_of_birth: date | None

    gender: str | None

    nationality: str | None

    nid_or_passport: str | None

    phone: str | None

    passenger_type: str

    created_at: str

    updated_at: str