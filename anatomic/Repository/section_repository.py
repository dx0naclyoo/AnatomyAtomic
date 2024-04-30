from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from anatomic import sql_tables
from anatomic.Database.database import postgresql, RedisTools
from anatomic.Repository.base import BaseRepository
from anatomic.tools import SortedMode, convert_pydantic_to_sql, is_sql_table
from anatomic.Backend.Section import model


class SectionRepository(BaseRepository):
    def __init__(self, session: AsyncSession = Depends(postgresql.get_session)):
        self.table = sql_tables.Section
        self.session: AsyncSession = session

    async def _get(self, section_id):
        sql = select(self.table).where(self.table.id == section_id)
        result = await self.session.execute(sql)
        if section := result.scalar():
            return section

    async def _get_by_name(self, name):
        sql = select(self.table).where(self.table.name == name)
        result = await self.session.execute(sql)
        if section := result.scalar():
            return section

    async def get_by_slug(self, slug):

        if f"section-{slug}" in [s.decode() for s in RedisTools.get_keys()]:
            print("by Slug REDIS")
            section = RedisTools.get(f"section-{slug}")
            dict_obj = eval("{" + section + "}")
            return model.Section.parse_obj(dict_obj)
        else:
            sql = select(self.table).where(self.table.slug == slug)
            result = await self.session.execute(sql)
            section = result.scalar()

            if section:
                print("by Slug Postgresql")
                RedisTools.set(f"section-{slug}", str(section.__repr__()))
                return section

    async def get_by_id(self, section_id):
        if f"section-{section_id}" in [s.decode() for s in RedisTools.get_keys()]:
            print("by ID REDIS")
            section = RedisTools.get(f"section-{section_id}")
            dict_obj = eval("{" + section + "}")
            return model.Section.parse_obj(dict_obj)
        else:
            print("by ID Postgresql")
            section = await self._get(section_id)
            if section:
                RedisTools.set(f"section-{section_id}", str(section.__repr__()))
                return section

    async def get_all(
            self, limit: int = 10, offset: int = 0, sorted_mode: SortedMode = SortedMode.ID
    ):
        sql = select(self.table).limit(limit).offset(offset)
        result = await self.session.execute(sql)
        sections = result.scalars().all()
        if sections:
            return sections

    async def create(self, section):
        if is_sql_table(section, self.table):
            sql_section = section
        else:
            sql_section = convert_pydantic_to_sql(section, self.table)

        _check = await self._get_by_name(sql_section.name)

        if not _check:
            self.session.add(sql_section)
            await self.session.commit()
            await self.session.refresh(sql_section)
            return sql_section

    async def update(self, section_id, section):
        old_section = await self._get(section_id)
        for key, value in section.dict().items():
            setattr(old_section, key, value)

        await self.session.commit()
        await self.session.refresh(old_section)
        return old_section

    async def delete(self, section_id):
        section = await self._get(section_id)

        if section:
            await self.session.delete(section)
            await self.session.commit()
            return True
        else:
            return False
