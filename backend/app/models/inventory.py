from sqlalchemy import ForeignKeyConstraint, Index, TIMESTAMP
from sqlalchemy.dialects.mysql import SMALLINT, TINYINT, MEDIUMINT
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base
import datetime

class Inventory(Base):
    __tablename__ = 'inventory'
    __table_args__ = (
        ForeignKeyConstraint(['film_id'], ['film.film_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_inventory_film'),
        ForeignKeyConstraint(['store_id'], ['store.store_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_inventory_store'),
        Index('idx_fk_film_id', 'film_id'),
        Index('idx_store_id_film_id', 'store_id', 'film_id'),
    )

    inventory_id: Mapped[int] = mapped_column(MEDIUMINT, primary_key=True)
    film_id: Mapped[int] = mapped_column(SMALLINT)
    store_id: Mapped[int] = mapped_column(TINYINT)
    last_update: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default='CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'
    )

    # 👇 Relación con Film
    film = relationship("Film", back_populates="inventory")
    rentals = relationship("Rental", back_populates="inventory")
