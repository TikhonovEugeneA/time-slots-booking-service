from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    async_sessionmaker,
)
from infrastructure.config import Settings


class DatabaseHelper:
    def __init__(self, settings: Settings) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=settings.database.url,
            echo=settings.database.echo,
            echo_pool=settings.database.echo_pool,
            pool_size=settings.database.pool_size,
            max_overflow=settings.database.max_overflow,
            pool_pre_ping=settings.database.pool_pre_ping,
            pool_recyle=settings.database.pool_recycle,
            pool_timeout=settings.database.pool_timeout,
        )

        self.session_factory: async_sessionmaker[AsyncEngine] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()
