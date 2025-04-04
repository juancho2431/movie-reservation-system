from sqlalchemy import ForeignKeyConstraint, Index, TIMESTAMP
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
import datetime

class FilmActor(Base):
    __tablename__ = 'film_actor'
    __table_args__ = (
        ForeignKeyConstraint(['actor_id'], ['actor.actor_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_film_actor_actor'),
        ForeignKeyConstraint(['film_id'], ['film.film_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_film_actor_film'),
        Index('idx_fk_film_id', 'film_id'),
    )

    actor_id: Mapped[int] = mapped_column(SMALLINT, primary_key=True)
    film_id: Mapped[int] = mapped_column(SMALLINT, primary_key=True)
    last_update: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default='CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'
    )
