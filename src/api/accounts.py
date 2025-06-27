from fastapi import APIRouter, HTTPException

from src.api.dependencies import UserIdDep

from src.database import async_session_maker
from src.repositories.accounts import AccountRepository
from src.repositories.users import UsersRepository
from src.schemas.accounts import Account
from src.schemas.users import UserRequestAdd, UserAdd, UserLogin, UserFullName, UserPatch
from src.services.auth import AuthService

router = APIRouter(prefix="/accounts", tags=["Счета"])

@router.get("/")
async def get_my_accounts(get_id: UserIdDep):
    async with async_session_maker() as session:
        accounts = await AccountRepository(session).get_my_accounts(user_id=get_id)
        return accounts

@router.get("/")
async def get_users_accounts(get_id:UserIdDep):
    async with async_session_maker() as session:
        users = await AccountRepository(session).get_my_accounts()
        return users