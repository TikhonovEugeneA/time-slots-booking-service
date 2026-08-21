from enum import Enum


class Role(str, Enum):
    CLIENT = "CLIENT"
    SPECIALIST = "SPECIALIST"
    ADMINISTRATOR = "ADMINISTRATOR"
