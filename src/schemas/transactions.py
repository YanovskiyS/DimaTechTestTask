from pydantic import BaseModel, UUID4


class HandleTransaction(BaseModel):
    transaction_id: str
    user_id: int
    account_id: int
    amount: int
    signature: str


class AddTransaction(BaseModel):
    id: UUID4
    user_id: int
    account_id: int
    amount: int

class TransactionForUser(BaseModel):
    id: UUID4
    account_id: int
    amount: int
