from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from anatomic import sql_tables
from anatomic.Backend.Section import model
from anatomic.Database.database import postgresql, RedisTools
from anatomic.Repository.base import BaseRepository
from anatomic.tools import SortedMode, convert_pydantic_to_sql, is_sql_table


class SubSectionRepository(BaseRepository):
    def __init__(self, session: AsyncSession = Depends(postgresql.get_session)):
        self.table = sql_tables.SubSection
        self.session: AsyncSession = session

    async def _get_by_id(self, subsection_id: int) -> sql_tables.SubSection:
        sql = select(self.table).where(self.table.id == subsection_id)
        response = await self.session.execute(sql)
        if subsection := response.scalar():
            return subsection

    async def _get_by_slug(self, subsection_slug: str) -> sql_tables.SubSection:
        sql = select(self.table).where(self.table.slug == subsection_slug)
        response = await self.session.execute(sql)
        if subsection := response.scalar():
            return subsection

    async def get_by_id(self, subsection_id: int):
        if f"subsection-{subsection_id}" in [s.decode() for s in RedisTools.get_keys()]:
            subsection = RedisTools.get(f"subsection-{subsection_id}")
            return subsection
        else:
            subsection = await self._get_by_id(subsection_id)
            RedisTools.set(f"subsection-{subsection_id}", subsection.__repr__())
            return subsection

    async def get_by_slug(self, subsection_slug: str):
        if f"subsection-{subsection_slug}" in [s.decode() for s in RedisTools.get_keys()]:
            subsection = RedisTools.get(f"subsection-{subsection_slug}")
            return subsection
        else:
            subsection = await self._get_by_slug(subsection_slug)
            RedisTools.set(f"subsection-{subsection_slug}", subsection.__repr__())
            return subsection

    async def get_all(self):
        pass

    async def create(self):
        pass

    async def update(self):
        pass

    async def delete(self):
        pass




