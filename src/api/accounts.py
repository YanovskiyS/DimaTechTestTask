from fastapi import APIRouter

from src.api.dependencies import UserIdDep, DbDep


router = APIRouter(prefix="/accounts", tags=["Счета"])

@router.get("/")
async def get_my_accounts_with_balance(get_id: UserIdDep, db:DbDep):
    accounts = await db.accounts.get_my_accounts(user_id=get_id)
    return accounts
