from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Numeric, Boolean
from sqlalchemy.orm import Mapped, mapped_column


class Account(BaseModel):
    id: int
    user_id: int
    balance: float
    is_active: bool

class AccountBalanceUpdate(BaseModel):
    user_id: int | None = Field(None)
    balance: float
    is_active: bool | None = Field(None)

class AccountForUser(BaseModel):
    id: int
    balance: float
