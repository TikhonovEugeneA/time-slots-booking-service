from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import DateTime, func


class CreatedAtMixin:
    __abstract__ = True

    created_at: Mapped[datetime]
