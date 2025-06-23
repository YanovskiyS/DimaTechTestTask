from pydantic import BaseModel, EmailStr, Field

class Transaction(BaseModel):
    transaction_id: str
    user_id: int
    account_id: int
    amount: float
    signature: str
