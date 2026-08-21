from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime


@dataclass
class Specialist:
    id: UUID = field(default_factory=uuid4)
    user_id: UUID
    center_id: UUID
    specialization: str
    is_available: bool = True
    created_at: datetime

    def create(self):
        self.specialization = self.specialization.strip()
