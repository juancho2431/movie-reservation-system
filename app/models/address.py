from sqlalchemy import Column, String, ForeignKeyConstraint, Index, TIMESTAMP, text
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import NullType  # 👈 solución aquí
from typing import Optional
from app.database import Base
import datetime

class Address(Base):
    __tablename__ = 'address'
    __table_args__ = (
        ForeignKeyConstraint(['city_id'], ['city.city_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_address_city'),
        Index('idx_fk_city_id', 'city_id'),
        Index('idx_location', 'location')
    )

    address_id: Mapped[int] = mapped_column(SMALLINT, primary_key=True)
    address: Mapped[str] = mapped_column(String(50))
    district: Mapped[str] = mapped_column(String(20))
    city_id: Mapped[int] = mapped_column(SMALLINT)
    phone: Mapped[str] = mapped_column(String(20))
    location: Mapped[Optional[bytes]] = mapped_column(NullType)  # ✅ corregido aquí
    last_update: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    address2: Mapped[Optional[str]] = mapped_column(String(50))
    postal_code: Mapped[Optional[str]] = mapped_column(String(10))
