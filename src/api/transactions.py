from fastapi import HTTPException, Response, Request
from fastapi import APIRouter

from src.schemas.transactions import Transaction
from src.services.transactions import calculate_signature

router = APIRouter(prefix="/webhook", tags=["Платежи"])

@router.post("/")
async def handle_webhook(request: Transaction):
    data =  request

    required_fields = {"transaction_id", "account_id", "user_id", "amount", "signature"}
    if not all(field in data for field in required_fields):
        raise HTTPException(status_code=400, detail="Не хватает обязательных полей")


    expected_signature = calculate_signature(*data)
    if data["signature"] != expected_signature:
        raise HTTPException(status_code=400, detail="Неверная подпись")

    transaction_id = data["transaction_id"]
    account_id = data["account_id"]
    user_id = data["user_id"]
    amount = data["amount"]



