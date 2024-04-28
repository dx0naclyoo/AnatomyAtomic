import asyncio

from fastapi import Depends, BackgroundTasks
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from anatomic.Database.database import postgresql, DatabaseSQL
from anatomic.Repository.base import BaseRepository
from anatomic import sql_tables


class UserRepository(BaseRepository):
    def __init__(self, session: AsyncSession = Depends(postgresql.get_session)):
        self.table = sql_tables.User
        self.session: AsyncSession = session

    async def get_by_id(self, user_id) -> sql_tables.User:
        stmt = select(self.table).where(self.table == user_id)
        response = await self.session.execute(stmt)
        if user := response.scalar():
            return user
        else:
            return sql_tables.User()

    async def get_all(self):
        pass

    async def create(self, user: sql_tables.User):

        self.session.add(user)
        await self.session.commit()
        return user

    async def update(self, user):
        pass

    async def delete(self, user_id):
        pass
