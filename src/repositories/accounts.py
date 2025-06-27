from pydantic import EmailStr, BaseModel
from sqlalchemy import select
from sqlalchemy.orm.sync import update

from src.models.accounts import AccountOrm
from src.models.transactions import TransactionsOrm

from src.repositories.base import BaseRepisitory
from src.schemas.accounts import Account
from src.schemas.transactions import AddTransaction



class AccountRepository(BaseRepisitory):
    model = AccountOrm
    schema = Account



    async def  update_balance(self, data: BaseModel,  **filter_by) -> None:

        product_update = (
            update(self.model)
            .filter_by(**filter_by)
            .values(data.model_dump())
        )
        await self.session.execute(product_update)

