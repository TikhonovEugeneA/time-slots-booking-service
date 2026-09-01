from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime
from ..shared.email import Email
from .user_role import UserRole


@dataclass
class User:
    id: UUID = field(default_factory=uuid4)
    name: str
    email: Email
    role: UserRole
    is_active: bool = True
    created_at: datetime
