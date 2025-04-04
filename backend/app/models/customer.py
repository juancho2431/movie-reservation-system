from sqlalchemy import Column, String, SmallInteger, DateTime, TIMESTAMP, ForeignKeyConstraint, Index, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from app.database import Base
import datetime

class Customer(Base):
    __tablename__ = 'customer'
    __table_args__ = (
        ForeignKeyConstraint(['address_id'], ['address.address_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_customer_address'),
        ForeignKeyConstraint(['store_id'], ['store.store_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_customer_store'),
        Index('idx_fk_address_id', 'address_id'),
        Index('idx_fk_store_id', 'store_id'),
        Index('idx_last_name', 'last_name')
    )

    customer_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    store_id: Mapped[int] = mapped_column(TINYINT)
    first_name: Mapped[str] = mapped_column(String(45))
    last_name: Mapped[str] = mapped_column(String(45))
    address_id: Mapped[int] = mapped_column(SmallInteger)
    active: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'1'"))
    create_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    email: Mapped[Optional[str]] = mapped_column(String(50))
    last_update: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    # ✅ Relación con Rental
    rentals = relationship("Rental", back_populates="customer")
