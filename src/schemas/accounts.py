from pydantic import BaseModel, Field


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
