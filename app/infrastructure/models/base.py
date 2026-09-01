from uuid import UUID
from uuid_utils.compat import uuid7
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy import TIMESTAMP


class Base(DeclarativeBase):
    __abstract__ = True

    type_annotation_map = {
        datetime: TIMESTAMP(timezone=True),
    }

    id: Mapped[UUID] = mapped_column(
        primary_key=True, autoincrement=True, default=uuid7
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"
