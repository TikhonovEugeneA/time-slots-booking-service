from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime
from .time_slot_status import TimeSlotStatus


@dataclass
class TimeSlot:
    id: UUID = field(default_factory=uuid4)
    specialist_id: UUID
    starts_at: datetime
    ends_at: datetime
    status: TimeSlotStatus = TimeSlotStatus.AVAILABLE
    created_at: datetime
