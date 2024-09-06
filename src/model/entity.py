from datetime import datetime
from sqlalchemy import DateTime, Identity
from sqlalchemy.orm import Mapped, DeclarativeBase
from sqlalchemy import Column, Integer, Text
from sqlalchemy.dialects.postgresql import ARRAY, FLOAT


class BaseEntity(DeclarativeBase):
    created_at: Mapped[datetime] = Column(DateTime(), server_default="DEFAULT", nullable=False)


class VectorEntity(BaseEntity):
    __tablename__ = "vectors"
    id: Mapped[int] = Column(Integer, Identity(), primary_key=True)
    vector: Mapped[list[float]] = Column(ARRAY(FLOAT(8)), nullable=False)
    text: Mapped[str] = Column(Text, nullable=False)
