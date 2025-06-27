from pydantic import BaseModel, EmailStr, Field

from src.schemas.accounts import Account, AccountForUser


class UserRequestAdd(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    is_admin: bool = Field(False)

class UserPatch(BaseModel):
    first_name: str | None = Field(None)
    last_name: str | None = Field(None)
    is_admin: bool | None = Field(False)
    email: EmailStr | None = Field(None)



class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserAdd(BaseModel):
    email: EmailStr
    hashed_password: str
    first_name: str
    last_name: str
    is_admin: bool


class User(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    is_admin: bool


class UserWithHashedPassword(User):
    hashed_password: str

class UserFullName(BaseModel):
    id: int
    email: EmailStr
    full_name: str

class UserWithRels(User):
    accounts: list[AccountForUser]