from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime
from domain.users.role import Role


@dataclass
class User:
    id: UUID = field(default_factory=uuid4)
    name: str
    email: str
    role: Role
    is_active: bool = True
    created_at: datetime
