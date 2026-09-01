from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import JSON


class MetadataMixin:
    __abstract__ = True

    metadata: Mapped[dict] = mapped_column(JSON, default=dict)
