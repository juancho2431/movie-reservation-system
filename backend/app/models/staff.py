from sqlalchemy import Column, String, ForeignKeyConstraint, Index, TIMESTAMP, text, VARCHAR
from sqlalchemy.dialects.mysql import TINYINT, SMALLINT
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from app.database import Base
import datetime

class Staff(Base):
    __tablename__ = 'staff'
    __table_args__ = (
        ForeignKeyConstraint(['address_id'], ['address.address_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_staff_address'),
        ForeignKeyConstraint(['store_id'], ['store.store_id'], ondelete='RESTRICT', onupdate='CASCADE', name='fk_staff_store'),
        Index('idx_fk_address_id', 'address_id'),
        Index('idx_fk_store_id', 'store_id')
    )

    staff_id: Mapped[int] = mapped_column(TINYINT, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(45))
    last_name: Mapped[str] = mapped_column(String(45))
    address_id: Mapped[int] = mapped_column(SMALLINT)
    store_id: Mapped[int] = mapped_column(TINYINT)
    active: Mapped[int] = mapped_column(TINYINT(1), server_default=text("'1'"))
    username: Mapped[str] = mapped_column(String(16))
    last_update: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    picture: Mapped[Optional[bytes]] = mapped_column()
    email: Mapped[Optional[str]] = mapped_column(String(50))
    password: Mapped[Optional[str]] = mapped_column(VARCHAR(40))
