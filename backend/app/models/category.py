from sqlalchemy import Column, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
import datetime

class Category(Base):
    __tablename__ = 'category'

    category_id: Mapped[int] = mapped_column(TINYINT, primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    last_update: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    )
