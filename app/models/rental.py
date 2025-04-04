from sqlalchemy import Column, DateTime, ForeignKeyConstraint, Index, Integer, TIMESTAMP, text
from sqlalchemy.dialects.mysql import MEDIUMINT, SMALLINT, TINYINT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from app.database import Base
import datetime

class Rental(Base):
    __tablename__ = 'rental'
    __table_args__ = (
        ForeignKeyConstraint(['customer_id'], ['customer.customer_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_rental_customer'),
        ForeignKeyConstraint(['inventory_id'], ['inventory.inventory_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_rental_inventory'),
        ForeignKeyConstraint(['staff_id'], ['staff.staff_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_rental_staff'),
        Index('idx_fk_customer_id', 'customer_id'),
        Index('idx_fk_inventory_id', 'inventory_id'),
        Index('idx_fk_staff_id', 'staff_id'),
        Index('rental_date', 'rental_date', 'inventory_id', 'customer_id', unique=True)
    )

    rental_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rental_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    inventory_id: Mapped[int] = mapped_column(MEDIUMINT)
    customer_id: Mapped[int] = mapped_column(SMALLINT)
    staff_id: Mapped[int] = mapped_column(TINYINT)
    last_update: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    return_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    # ✅ Relaciones necesarias
    inventory = relationship("Inventory", back_populates="rentals")
    customer = relationship("Customer", back_populates="rentals")
