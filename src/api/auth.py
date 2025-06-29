from fastapi import HTTPException, Response
from fastapi import APIRouter


from src.api.dependencies import UserIdDep

from src.database import async_session_maker
from src.repositories.users import UsersRepository
from src.schemas.users import UserLogin, UserFullName
from src.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Авторизация"])


@router.post("/login")
async def login_user(data: UserLogin, response: Response):
    async with async_session_maker() as session:
        user = await UsersRepository(session).get_user_with_hashed_password(
            email=data.email
        )
        if not user:
            raise HTTPException(
                status_code=401, detail="Пользователь с таким email не зарегестрирован"
            )
        if not AuthService().verify_password(data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Пароль не верный")
        access_token = AuthService().create_access_token({"user_id": user.id})
        response.set_cookie("access_token", access_token)
        return {"access_token": access_token}


@router.get("/me")
async def get_me(user_id: UserIdDep):
    async with async_session_maker() as session:
        data = await UsersRepository(session).get_one_or_none(id=user_id)
        new_user = UserFullName(
            id=data.id,
            email=data.email,
            full_name=f"{data.first_name} {data.last_name}",
        )
        return new_user
