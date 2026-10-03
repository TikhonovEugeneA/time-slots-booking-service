from typing import Protocol
from .service_center import ServiceCenter


class IServiceCenterRepository(Protocol):

    async def add(self, service_center: ServiceCenter) -> ServiceCenter: ...
