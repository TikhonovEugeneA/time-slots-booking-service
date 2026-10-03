from sqlalchemy.ext.asyncio import AsyncSession

from domain.service_centers.repository import IServiceServiceRepository
from domain.service_centers.service_center import ServiceCenter


class ServiceCenterRepositoryImplementayion(IServiceServiceRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add(self, service_center: ServiceCenter) -> ServiceCenter:

        pass
