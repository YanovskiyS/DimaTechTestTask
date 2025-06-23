from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, ForeignKey, Numeric

from src.database import Base


class TransactionsOrm(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Numeric, nullable=False)
    status: Mapped[str] = mapped_column(String(20), default='COMPLETED')

    account = relationship("AccountOrm", back_populates="transactions")
    user = relationship("UserOrm", back_populates="transactions")