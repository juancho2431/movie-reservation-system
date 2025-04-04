from sqlalchemy import Column, String, TIMESTAMP, Index, text
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
import datetime

class Actor(Base):
    __tablename__ = 'actor'
    __table_args__ = (
        Index('idx_actor_last_name', 'last_name'),
    )

    actor_id: Mapped[int] = mapped_column(SMALLINT, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(45))
    last_name: Mapped[str] = mapped_column(String(45))
    last_update: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    )
