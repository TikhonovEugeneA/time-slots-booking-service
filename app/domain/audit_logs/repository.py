from typing import Protocol
from uuid import UUID
from .audit_log import AuditLog


class IAuditLogRepository(Protocol):

    async def add(self, audit_log: AuditLog) -> None: ...

    async def get_by_id(self, audit_log_id: UUID) -> AuditLog: ...

    async def get_all(self) -> list[AuditLog]: ...
