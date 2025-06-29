from src.repositories.accounts import AccountRepository
from src.repositories.transactions import TransactionRepository
from src.repositories.users import UsersRepository


class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.accounts = AccountRepository(self.session)
        self.transactions = TransactionRepository(self.session)
        self.users = UsersRepository(self.session)

        return self

    async def __aexit__(self, *args):
        self.session.rollback()
        self.session.close()

    async def commit(self):
        await self.session.commit()
