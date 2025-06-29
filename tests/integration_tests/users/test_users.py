from pydantic import EmailStr

from src.database import async_session_maker
from src.schemas.users import UserRequestAdd, UserAdd
from src.services.auth import AuthService
from src.utils.db_manager import DBManager


async def test_add_user():
    user_request = UserRequestAdd(email="test_user@example.ru", password="123456",
                                  first_name="test", last_name="user", is_admin=False)
    hashed_password = AuthService().hashed_password(user_request.password)
    user_data = UserAdd(email="test_user@example.ru", hashed_password=hashed_password,
                        first_name="test", last_name="user", is_admin=False)


    async with DBManager(session_factory=async_session_maker) as db:
        await db.users.add(user_data)
        await db.commit()

