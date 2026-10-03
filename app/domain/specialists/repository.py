from typing import Protocol
from .specialist import Specialist


class ISpecialistRepository(Protocol):

    async def add(self, specialist: Specialist) -> None: ...
