from fastapi import HTTPException, Response, Request

from fastapi import APIRouter
from sqlalchemy import update

from src.api.dependencies import UserIdDep

from src.database import async_session_maker
from src.repositories.users import UsersRepository
from src.schemas.users import UserRequestAdd, UserAdd, UserLogin, UserFullName, UserPatch
from src.services.auth import AuthService

router = APIRouter(prefix="/users", tags=["Пользователи"])

@router.post("/add")
async def add_user(data: UserRequestAdd, get_id: UserIdDep):
    hashed_password = AuthService().hashed_password(data.password)
    new_user_data = UserAdd(email=data.email, first_name=data.first_name,
                            last_name=data.last_name,
                            hashed_password=hashed_password,
                            is_admin=data.is_admin)
    async with async_session_maker() as session:
        user = await UsersRepository(session).get_one_or_none(id=get_id)
        if user.is_admin:
            await UsersRepository(session).add(new_user_data)
            await session.commit()
            return {"status": "ok"}
        else:
            raise HTTPException(status_code=401, detail="Добавлять пользователя может только администратор")


@router.patch("/{user_id}")
async def update_user(user_id: int, user_data: UserPatch, get_id:UserIdDep):
    async with async_session_maker() as session:
        user = await UsersRepository(session).get_one_or_none(id=get_id)
        if user.is_admin:
            await UsersRepository(session).edit(user_data, id=user_id)
            await session.commit()
            return {"status": "Ok"}
        else:
            raise HTTPException(status_code=401, detail="Изменять пользователя может только администратор")



@router.delete("/{user_id}")
async def delete_hotel(user_id: int, get_id:UserIdDep):
    async with async_session_maker() as session:
        user = await UsersRepository(session).get_one_or_none(id=get_id)
        if user.is_admin:
            await UsersRepository(session).delete(id=user_id)
            await session.commit()
            return {"status": "Ok"}
        else:
            raise HTTPException(status_code=401, detail="Удалять пользователя может только администратор")





