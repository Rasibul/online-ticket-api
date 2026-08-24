from enum import Enum


class UserRole(str, Enum):
    USER = "USER"
    BUS = "BUS-ADMIN"
    TRAIN = "TRAIN-ADMIN"
    AIRPLANE = "AIRPLANE-ADMIN"