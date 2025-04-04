from sqlalchemy import Column, CHAR, TIMESTAMP, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
import datetime

class Language(Base):
    __tablename__ = 'language'

    language_id: Mapped[int] = mapped_column(TINYINT, primary_key=True)
    name: Mapped[str] = mapped_column(CHAR(20))
    last_update: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    )
