from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime
from domain.time_slots.time_slot_status import Status


@dataclass
class TimeSlot:
    id: UUID = field(default_factory=uuid4)
    starts_at: datetime
    ends_at: datetime
    status: Status = Status.AVAILABLE
    created_at: datetime

    def is_blocked():
        pass

    def blocked():
        pass

    def unblock():
        pass
