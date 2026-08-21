from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict
from uuid import UUID, uuid4


@dataclass
class AuditLog:
    id: UUID = field(default_factory=uuid4)
    booking_id: UUID
    action: str
    actor_id: UUID
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime
