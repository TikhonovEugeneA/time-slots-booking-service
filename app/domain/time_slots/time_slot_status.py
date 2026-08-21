from enum import Enum


class Status(str, Enum):
    AVAILABLE = "AVAILABLE"
    BLOCKED = "BLOCKED"
