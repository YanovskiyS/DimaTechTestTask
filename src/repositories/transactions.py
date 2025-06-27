from pydantic import EmailStr
from sqlalchemy import select

from src.models.transactions import TransactionsOrm

from src.repositories.base import BaseRepisitory
from src.schemas.transactions import AddTransaction



class TransactionRepository(BaseRepisitory):
    model = TransactionsOrm
    schema = AddTransaction
