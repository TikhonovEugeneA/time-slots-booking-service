from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    value: str
