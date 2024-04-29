from fastapi import Depends, HTTPException, status
from fastapi.exceptions import ResponseValidationError
from sqlalchemy import select
from sqlalchemy.exc import MissingGreenlet
from sqlalchemy.ext.asyncio import AsyncSession

from anatomic.Database.database import postgresql, DatabaseSQL
from anatomic.Repository.base import BaseRepository
from anatomic import sql_tables
from anatomic.tools import SortedMode, convert_pydantic_to_sql, is_sql_table


class SectionRepository(BaseRepository):
    def __init__(self, session: AsyncSession = Depends(postgresql.get_session)):
        self.table = sql_tables.Section
        self.session: AsyncSession = session

    async def get(self, section_id):
        sql = select(self.table).where(self.table.id == section_id)

        result = await self.session.execute(sql)
        section = result.scalar()

        if section:
            return section
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Section not found"
            )

    async def get_all(
        self, limit: int = 10, offset: int = 0, sorted_mode: SortedMode = SortedMode.ID
    ):
        sql = select(self.table).limit(limit).offset(offset)
        result = await self.session.execute(sql)
        sections = result.scalars().all()
        if sections:
            return sections
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Sections not found"
            )

    async def create(self, section):
        if is_sql_table(section, self.table):
            sql_section = section
        else:
            sql_section = convert_pydantic_to_sql(section, self.table)

        self.session.add(sql_section)
        await self.session.commit()
        await self.session.refresh(sql_section)
        return sql_section

    async def update(self, section_id, section):
        old_section = await self.get(section_id)
        for key, value in section.dict().items():
            setattr(old_section, key, value)

        await self.session.commit()
        await self.session.refresh(old_section)
        return old_section

    async def delete(self, section_id):
        section = await self.get(section_id)

        if section:
            await self.session.cascade_delete(section)
            await self.session.commit()
            return True
        else:
            return False
