from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime
from ..shared.email import Email
from .user_role import UserRole


@dataclass
class User:
    name: str
    email: Email
    role: UserRole
    created_at: datetime
    id: UUID = field(default_factory=uuid4)
    is_active: bool = True
