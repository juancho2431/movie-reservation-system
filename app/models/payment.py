from sqlalchemy import Column, DateTime, DECIMAL, ForeignKeyConstraint, Index, Integer, SmallInteger, TIMESTAMP, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from app.database import Base
import datetime
import decimal

class Payment(Base):
    __tablename__ = 'payment'
    __table_args__ = (
        ForeignKeyConstraint(['customer_id'], ['customer.customer_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_payment_customer'),
        ForeignKeyConstraint(['rental_id'], ['rental.rental_id'], ondelete='SET NULL', onupdate='CASCADE', name='fk_payment_rental'),
        ForeignKeyConstraint(['staff_id'], ['staff.staff_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_payment_staff'),
        Index('fk_payment_rental', 'rental_id'),
        Index('idx_fk_customer_id', 'customer_id'),
        Index('idx_fk_staff_id', 'staff_id')
    )

    payment_id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    customer_id: Mapped[int] = mapped_column(SmallInteger)
    staff_id: Mapped[int] = mapped_column(TINYINT)
    amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(5, 2))
    payment_date: Mapped[datetime.datetime] = mapped_column(DateTime)
    rental_id: Mapped[Optional[int]] = mapped_column(Integer)
    last_update: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
