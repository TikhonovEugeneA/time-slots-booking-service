from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime


@dataclass
class ServiceCenter:
    id: UUID = field(default_factory=uuid4)
    name: str
    address: str
    timezone: str
    is_active: bool = True
    created_at: datetime
