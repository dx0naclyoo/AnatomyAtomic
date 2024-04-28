from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from anatomic.Database.database import postgresql, DatabaseSQL
from anatomic.Repository.base import BaseRepository
from anatomic import sql_tables


class SectionRepository(BaseRepository):
    def __init__(self, session: AsyncSession = Depends(postgresql.get_session)):
        self.table = sql_tables.Section
        self.session: AsyncSession = session

    def get(self):
        pass

    def get_all(self):
        pass

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
