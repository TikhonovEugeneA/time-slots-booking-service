from uuid import UUID
from .user import User
from typing import Protocol


class IUserRepository(Protocol):

    async def get_by_id(self, user_id: UUID) -> User: ...
