from sqlalchemy import Column, String, ForeignKeyConstraint, Index, TIMESTAMP, text
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
import datetime

class City(Base):
    __tablename__ = 'city'
    __table_args__ = (
        ForeignKeyConstraint(['country_id'], ['country.country_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_city_country'),
        Index('idx_fk_country_id', 'country_id')
    )

    city_id: Mapped[int] = mapped_column(SMALLINT, primary_key=True)
    city: Mapped[str] = mapped_column(String(50))
    country_id: Mapped[int] = mapped_column(SMALLINT)
    last_update: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
