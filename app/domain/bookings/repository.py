from typing import Protocol
from uuid import UUID
from .booking import Booking


class IBookingRepository(Protocol):

    async def add(self, booking: Booking) -> None: ...

    async def get_by_id(self, booking_id: UUID) -> Booking: ...

    async def get_all(self) -> list[Booking]: ...
