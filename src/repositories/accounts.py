from sqlalchemy import select


from src.models.accounts import AccountOrm
from src.repositories.base import BaseRepository
from src.schemas.accounts import Account, AccountForUser


class AccountRepository(BaseRepository):
    model = AccountOrm
    schema = Account

    async def get_my_accounts(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        return [
            AccountForUser.model_validate(model, from_attributes=True)
            for model in result.scalars().all()
        ]
