from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4
from .booking_status import BookingStatus


@dataclass
class Booking:
    slot_id: UUID
    client_id: UUID
    subject: str
    created_at: datetime
    updated_at: datetime
    cancelled_at: datetime | None = None
    completed_at: datetime | None = None
    id: UUID = field(default_factory=uuid4)
    status: BookingStatus = BookingStatus.BOOKED
