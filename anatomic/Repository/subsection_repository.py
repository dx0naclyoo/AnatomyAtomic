from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from anatomic import sql_tables
from anatomic.Backend.SubSection import model
from anatomic.Database.database import postgresql, RedisTools
from anatomic.Repository.base import BaseRepository
from anatomic.tools import redis_to_pydantic, convert_pydantic_to_sql


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
            it = redis_to_pydantic(model=model.SubSection, redis_item=subsection)
            return it
        else:
            subsection = await self._get_by_id(subsection_id)
            if subsection:
                RedisTools.set(f"subsection-{subsection_id}", subsection.__repr__())
                return subsection

    async def get_by_slug(self, subsection_slug: str):
        if f"subsection-{subsection_slug}" in [
            s.decode() for s in RedisTools.get_keys()
        ]:
            subsection = RedisTools.get(f"subsection-{subsection_slug}")
            it = redis_to_pydantic(model=model.SubSection, redis_item=subsection)
            return it
        else:
            subsection = await self._get_by_slug(subsection_slug)
            if subsection:
                RedisTools.set(f"subsection-{subsection_slug}", subsection.__repr__())
                return subsection

    async def get_all(
        self,
        limit: int = 10,
        offset: int = 0,
        section_id: int = None,
    ):
        if section_id:
            sql = (
                select(self.table)
                .where(self.table.section_id == section_id)
                .limit(limit)
                .offset(offset)
            )
        else:
            sql = select(self.table).limit(limit).offset(offset)

        response = await self.session.execute(sql)
        subsections = response.scalars().all()
        if subsections:
            return subsections
        else:
            return []

    async def create(self, subsection: model.SubSectionCreate):
        sql_subsection = convert_pydantic_to_sql(subsection, self.table)

        _check = await self._get_by_slug(sql_subsection.slug)

        if _check is None:
            self.session.add(sql_subsection)
            await self.session.commit()
            await self.session.refresh(sql_subsection)
            return sql_subsection

    async def update(
        self, old_subsection: int, subsection_new: model.SubSectionUpdateBackendOnly
    ):
        if old_subsection:
            for key, value in subsection_new.dict().items():
                setattr(old_subsection, key, value)

            if f"subsection-{old_subsection.slug}" in [
                s.decode() for s in RedisTools.get_keys()
            ]:
                RedisTools.delete(f"subsection-{old_subsection.slug}")
            if f"subsection-{old_subsection.id}" in [
                s.decode() for s in RedisTools.get_keys()
            ]:
                RedisTools.delete(f"subsection-{old_subsection.id}")

            await self.session.commit()
            await self.session.refresh(old_subsection)
            return old_subsection

    async def delete(self, subsection_id: int):
        subsection = await self._get_by_id(subsection_id)

        if subsection:
            slug = subsection.slug
            await self.session.delete(subsection)
            await self.session.commit()

            if f"subsection-{slug}" in [s.decode() for s in RedisTools.get_keys()]:
                RedisTools.delete(f"subsection-{slug}")
            if f"subsection-{subsection_id}" in [
                s.decode() for s in RedisTools.get_keys()
            ]:
                RedisTools.delete(f"subsection-{subsection_id}")
