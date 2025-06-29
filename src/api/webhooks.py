from fastapi import HTTPException
from fastapi import APIRouter
from uuid import UUID


from src.api.dependencies import DbDep
from src.schemas.accounts import Account
from src.schemas.transactions import AddTransaction, HandleTransaction
from src.services.transactions import calculate_signature

router = APIRouter(prefix="/webhook", tags=["Обработка платежа"])


@router.post("/")
async def handle_webhook(webhook: HandleTransaction, db: DbDep):
    data = webhook.model_dump()

    expected_signature = calculate_signature(data)
    if data["signature"] != expected_signature:
        raise HTTPException(status_code=400, detail="Неверная подпись")

    uuid_obj = UUID(webhook.transaction_id)
    transaction = await db.transactions.get_one_or_none(id=uuid_obj)
    if transaction:
        raise HTTPException(status_code=400, detail="Транзакция уже обработана")

    account = await db.accounts.get_one_or_none(user_id=webhook.user_id)
    if account is None:
        new_account = Account(user_id=webhook.user_id, balance=0, is_active=True)
        await db.accounts.add(new_account)
        await db.commit()

    transaction = AddTransaction(
        id=webhook.transaction_id,
        user_id=webhook.user_id,
        account_id=webhook.account_id,
        amount=webhook.amount,
    )

    account = await db.accounts.get_one_or_none(user_id=webhook.user_id)

    new_balance = account.balance + webhook.amount

    new_account = Account(
        id=webhook.user_id,
        user_id=account.user_id,
        balance=new_balance,
        is_active=account.is_active,
    )

    await db.accounts.edit(new_account)
    await db.transactions.add(transaction)
    await db.commit()
    return {"status": "OK", "detail": "Транзакция обработана"}
