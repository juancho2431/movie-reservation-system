from sqlalchemy import Column, String, Text, Index
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class FilmText(Base):
    __tablename__ = 'film_text'
    __table_args__ = (
        Index('idx_title_description', 'title', 'description'),
    )

    film_id: Mapped[int] = mapped_column(SMALLINT, primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
