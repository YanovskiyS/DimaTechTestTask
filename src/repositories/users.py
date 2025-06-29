from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.models.users import UsersOrm
from src.repositories.base import BaseRepository
from src.schemas.users import User, UserWithHashedPassword, UserWithRels


class UsersRepository(BaseRepository):
    model = UsersOrm
    schema = User

    async def get_user_with_hashed_password(self, email: EmailStr):
        query = select(self.model).filter_by(email=email)
        result = await self.session.execute(query)
        model = result.scalar_one()
        return UserWithHashedPassword.model_validate(model, from_attributes=True)

    async def get_users_with_accounts(self):
        query = select(self.model).options(selectinload(self.model.accounts))
        result = await self.session.execute(query)
        models = result.scalars().all()
        return [
            UserWithRels.model_validate(model, from_attributes=True) for model in models
        ]

    async def get_filtered(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        return [
            self.schema.model_validate(model, from_attributes=True)
            for model in result.scalars().all()
        ]
