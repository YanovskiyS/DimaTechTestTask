from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import String, Boolean, ForeignKey, Numeric

from src.database import Base


class AccountOrm(Base):
    __tablename__ = 'accounts'

    id: Mapped[int] =  mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    balance: Mapped[float] = mapped_column(Numeric(15, 2), nullable=False, default=0.00)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    user = relationship("User", back_populates="accounts")
    transactions = relationship("TransactionOrm", back_populates="account", cascade="all, delete-orphan")
