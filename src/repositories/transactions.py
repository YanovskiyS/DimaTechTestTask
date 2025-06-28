from pydantic import EmailStr
from sqlalchemy import select

from src.models.transactions import TransactionsOrm

from src.repositories.base import BaseRepository
from src.schemas.transactions import AddTransaction, TransactionForUser


class TransactionRepository(BaseRepository):
    model = TransactionsOrm
    schema = AddTransaction


    async def get_my_transactions(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        return [TransactionForUser.model_validate(model, from_attributes=True) for model in result.scalars().all()]