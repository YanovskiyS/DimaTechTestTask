from fastapi import HTTPException, Response, Request
from fastapi import APIRouter
from uuid import UUID

from sqlalchemy.util import await_only

from src.api.dependencies import UserIdDep
from src.database import async_session_maker
from src.repositories.accounts import AccountRepository
from src.repositories.transactions import TransactionRepository
from src.schemas.accounts import Account, AccountBalanceUpdate
from src.schemas.transactions import AddTransaction, HandleTransaction
from src.services.transactions import calculate_signature

router = APIRouter(prefix="/webhook", tags=["Платежи"])

@router.post("/")
async def handle_webhook(webhook: HandleTransaction):
    data =  webhook.model_dump()

    expected_signature = calculate_signature(data)
    if data["signature"] != expected_signature:
        raise HTTPException(status_code=400, detail="Неверная подпись")

    async with async_session_maker() as session:
        uuid_obj = UUID(webhook.transaction_id)
        transaction = await TransactionRepository(session).get_one_or_none(id=uuid_obj)
        if transaction:
            raise HTTPException(status_code=400, detail="Транзакция уже обработана")


    async with async_session_maker() as session:
        account = await AccountRepository(session).get_one_or_none(user_id=webhook.user_id)
        if account is None:
            new_account = Account(user_id=webhook.user_id, balance=0, is_active=True)
            await AccountRepository(session).add(new_account)
            await session.commit()

    async with async_session_maker() as session:
        transaction = AddTransaction(id=webhook.transaction_id,
                                  user_id=webhook.user_id,
                                  account_id=webhook.account_id,
                                  amount=webhook.amount)

        account = await AccountRepository(session).get_one_or_none(user_id=webhook.user_id)

        new_balance = account.balance + webhook.amount

        new_account = Account(user_id=account.user_id, balance=new_balance, is_active=account.is_active)

        await AccountRepository(session).edit(new_account)
        await TransactionRepository(session).add(transaction)
        await session.commit()
        return {"status": "OK", "detail": "Транзакция обработана"}




@router.get("/")
async def get_my_transactions(get_id: UserIdDep):
    async with async_session_maker() as session:
        result = await TransactionRepository(session).get_filtered(user_id=get_id)
        return result















