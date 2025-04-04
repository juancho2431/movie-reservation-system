from sqlalchemy import ForeignKeyConstraint, Index, TIMESTAMP, SmallInteger
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
import datetime

class FilmCategory(Base):
    __tablename__ = 'film_category'
    __table_args__ = (
        ForeignKeyConstraint(['category_id'], ['category.category_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_film_category_category'),
        ForeignKeyConstraint(['film_id'], ['film.film_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_film_category_film'),
        Index('fk_film_category_category', 'category_id'),
    )

    film_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    category_id: Mapped[int] = mapped_column(TINYINT, primary_key=True)
    last_update: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default='CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'
    )
