from fastapi import APIRouter, HTTPException


from src.api.dependencies import UserIdDep, DbDep
from src.schemas.users import UserRequestAdd, UserAdd, UserLogin, UserFullName, UserPatch
from src.services.auth import AuthService

router = APIRouter(prefix="/users", tags=["Пользователи"])

@router.post("/add")
async def add_user(data: UserRequestAdd, get_id: UserIdDep, db:DbDep):
    hashed_password = AuthService().hashed_password(data.password)
    new_user_data = UserAdd(email=data.email, first_name=data.first_name,
                            last_name=data.last_name,
                            hashed_password=hashed_password,
                            is_admin=data.is_admin)

    user = await db.users.get_one_or_none(id=get_id)
    if user.is_admin:
        await db.users.add(new_user_data)
        await db.commit()
        return {"status": "ok"}
    else:
        raise HTTPException(status_code=401, detail="Вы не аторизованы как администратор")


@router.patch("/{user_id}")
async def update_user(user_id: int, user_data: UserPatch, get_id:UserIdDep, db:DbDep):
    user = await db.users.get_one_or_none(id=get_id)
    if user.is_admin:
        await db.users.edit(user_data, id=user_id)
        await db.commit()
        return {"status": "Ok"}
    else:
        raise HTTPException(status_code=401, detail="Вы не аторизованы как администратор")


@router.delete("/{user_id}")
async def delete_user(user_id: int, get_id:UserIdDep, db: DbDep):

    user = await db.users.get_one_or_none(id=get_id)
    if user.is_admin:
        await db.users.delete(id=user_id)
        await db.commit()
        return {"status": "Ok"}
    else:
        raise HTTPException(status_code=401, detail="УВы не аторизованы как администратор")


@router.get("/")
async def get_users_with_accounts(db: DbDep, get_id:UserIdDep):
    user = await db.users.get_one_or_none(id=get_id)
    if user.is_admin:
        users = await db.users.get_users_with_accounts()
        return users
    else:
        raise HTTPException(status_code=401, detail="Вы не аторизованы как администратор")



