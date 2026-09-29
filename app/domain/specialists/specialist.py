from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime


@dataclass
class Specialist:
    user_id: UUID
    center_id: UUID
    specialization: str
    created_at: datetime
    id: UUID = field(default_factory=uuid4)
    is_available: bool = True
