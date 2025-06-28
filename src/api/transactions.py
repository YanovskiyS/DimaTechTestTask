from fastapi import APIRouter

from src.api.dependencies import UserIdDep, DbDep

router = APIRouter(prefix="/transactions", tags=["Транзакции"])


@router.get("/")
async def get_my_transactions(get_id: UserIdDep, db: DbDep):
    result = await db.transactions.get_my_transactions(user_id=get_id)
    return result















