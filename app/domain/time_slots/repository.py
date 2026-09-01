from typing import Protocol
from domain.time_slots.time_slot import TimeSlot
from uuid import UUID


class ITimeSlotRepository(Protocol):

    async def add(self, time_slot: TimeSlot) -> None: ...

    async def get_by_id(self, time_slot_id: UUID) -> TimeSlot: ...

    async def get_all(self) -> list[TimeSlot]: ...

    async def update(self, time_slot: TimeSlot): ...
