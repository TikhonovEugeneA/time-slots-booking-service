from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4
from domain.bookings.booking_status import BookingStatus


@dataclass
class Booking:
    id: UUID = field(default_factory=uuid4)
    slot_id: UUID
    client_id: UUID
    subject: str
    status: BookingStatus
    created_at: datetime
    updated_at: datetime
    cancelled_at: datetime | None = None
    completed_at: datetime | None = None

    @classmethod
    def book(cls, slot_id: UUID, client_id: UUID, subject: str) -> "Booking":

        return cls(
            id=None,
            slot_id=slot_id,
            client_id=client_id,
            subject=subject,
            status=BookingStatus.BOOKED,
            created_at=None,
        )
