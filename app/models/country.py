from sqlalchemy import Column, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
import datetime

class Country(Base):
    __tablename__ = 'country'

    country_id: Mapped[int] = mapped_column(SMALLINT, primary_key=True)
    country: Mapped[str] = mapped_column(String(50))
    last_update: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    )
