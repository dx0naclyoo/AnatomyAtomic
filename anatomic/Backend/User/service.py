from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from anatomic import sql_tables
from anatomic.Database.database import postgresql
from anatomic.Repository.user_repository import UserRepository
from anatomic.Backend.User import model


class UserService:
    def __init__(self, user_repository: UserRepository = Depends(UserRepository)):
        self.user_repository = user_repository

    async def get_self(self):
        pass

    async def get_user(self, user_id):
        return await self.user_repository.get_by_id(user_id)

    async def get_all_users(self):
        return await self.user_repository.get_all()

    async def add_user(self, user: model.UserRegister):

        sql_user = sql_tables.User(**user.dict())

        return await self.user_repository.create(sql_user)
