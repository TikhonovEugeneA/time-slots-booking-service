from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime


@dataclass
class ServiceCenter:
    name: str
    address: str
    timezone: str
    created_at: datetime
    id: UUID = field(default_factory=uuid4)
    is_active: bool = True
