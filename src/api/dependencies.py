from typing import Annotated
from fastapi import Depends, Request, HTTPException

from src.database import async_session_maker
from src.services.auth import AuthService
from src.utils.db_manager import DBManager


def get_token(request: Request):
    token = request.cookies.get("access_token", None)
    if not token:
        raise HTTPException(status_code=401, detail="Вы не предоставили токен")
    return token


def get_current_user_id(token: str = Depends(get_token)):
    data = AuthService().decode_token(token)
    return data["user_id"]


UserIdDep = Annotated[int, Depends(get_current_user_id)]


async def get_db():
    async with DBManager(session_factory=async_session_maker) as db:
        yield db


DbDep = Annotated[DBManager, Depends(get_db)]
