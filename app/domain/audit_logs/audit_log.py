from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict
from uuid import UUID, uuid4


@dataclass
class AuditLog:
    booking_id: UUID
    action: str
    actor_id: UUID
    created_at: datetime
    id: UUID = field(default_factory=uuid4)
    metadata: Dict[str, Any] = field(default_factory=dict)
