from sqlalchemy import Column, ForeignKeyConstraint, Index, SmallInteger, TIMESTAMP, text
from sqlalchemy.dialects.mysql import TINYINT  # ✅ Corrección aquí
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
import datetime

class Store(Base):
    __tablename__ = 'store'
    __table_args__ = (
        ForeignKeyConstraint(['address_id'], ['address.address_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_store_address'),
        ForeignKeyConstraint(['manager_staff_id'], ['staff.staff_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_store_staff'),
        Index('idx_fk_address_id', 'address_id'),
        Index('idx_unique_manager', 'manager_staff_id', unique=True)
    )

    store_id: Mapped[int] = mapped_column(TINYINT, primary_key=True)
    manager_staff_id: Mapped[int] = mapped_column(TINYINT)
    address_id: Mapped[int] = mapped_column(SmallInteger)
    last_update: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
