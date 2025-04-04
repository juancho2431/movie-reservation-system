from __future__ import annotations


from sqlalchemy import Column, String, SmallInteger, Text, DECIMAL, Enum, ForeignKeyConstraint, Index, TIMESTAMP, text
from sqlalchemy.dialects.mysql import SET  # ✅ SET importado correctamente
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional, List, Any
from app.database import Base
import datetime
import decimal


from app.models.inventory import Inventory



class Film(Base):
    __tablename__ = 'film'
    __table_args__ = (
        ForeignKeyConstraint(['language_id'], ['language.language_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_film_language'),
        ForeignKeyConstraint(['original_language_id'], ['language.language_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_film_language_original'),
        Index('idx_fk_language_id', 'language_id'),
        Index('idx_fk_original_language_id', 'original_language_id'),
        Index('idx_title', 'title')
    )

    film_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    title: Mapped[str] = mapped_column(String(128))
    language_id: Mapped[int] = mapped_column(SmallInteger)
    rental_duration: Mapped[int] = mapped_column(SmallInteger, server_default=text("'3'"))
    rental_rate: Mapped[decimal.Decimal] = mapped_column(DECIMAL(4, 2), server_default=text("'4.99'"))
    replacement_cost: Mapped[decimal.Decimal] = mapped_column(DECIMAL(5, 2), server_default=text("'19.99'"))
    last_update: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    description: Mapped[Optional[str]] = mapped_column(Text)
    release_year: Mapped[Optional[Any]] = mapped_column(String(4))
    original_language_id: Mapped[Optional[int]] = mapped_column(SmallInteger)
    length: Mapped[Optional[int]] = mapped_column(SmallInteger)
    rating: Mapped[Optional[str]] = mapped_column(Enum('G', 'PG', 'PG-13', 'R', 'NC-17'), server_default=text("'G'"))
    special_features: Mapped[Optional[str]] = mapped_column(
        SET('Trailers', 'Commentaries', 'Deleted Scenes', 'Behind the Scenes')
    )

    # Relaciones
    inventory: Mapped[List["Inventory"]] = relationship("Inventory", back_populates="film")
