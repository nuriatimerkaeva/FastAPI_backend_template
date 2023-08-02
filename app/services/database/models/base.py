from typing import Optional
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr, as_declarative
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped


@as_declarative()
class Base:

    __abstract__: bool = True

    @declared_attr
    def __tablename__(self) -> str:
        return type(self).__name__.lower()


class BaseWithIdAndTime:

    id: Mapped[Optional[UUID]] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=uuid.uuid4)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now,
    )
