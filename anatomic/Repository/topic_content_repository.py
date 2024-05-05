from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from anatomic import sql_tables
from anatomic.Database.database import postgresql, RedisTools
from anatomic.Repository.base import BaseRepository
from anatomic.tools import redis_to_pydantic, convert_pydantic_to_sql

from anatomic.Backend.TopicContent import model


class TopicContentRepository():

    def __init__(self, session: AsyncSession = Depends(postgresql.get_session)):
        self.table = sql_tables.TopicContent
        self.session: AsyncSession = session

    async def _get_by_id(self, content_id):
        sql = select(self.table).where(self.table.id == content_id)
        response = await self.session.execute(sql)
        if subsection := response.scalar():
            return subsection

    async def get(self, content_id):

        if f"content-{content_id}" in [s.decode() for s in RedisTools.get_keys()]:
            content = RedisTools.get(f"content-{content_id}")
            it = redis_to_pydantic(model=model.Content, redis_item=content)
            return it
        else:
            content = await self._get_by_id(content_id)

            if content:
                RedisTools.set(f"content-{content_id}", content.__repr__())
                return content

    async def get_all(self):
        sql = select(self.table)
        response = await self.session.execute(sql)
        subsections = response.scalars().all()
        if subsections:
            return subsections
        else:
            return []

    async def create(self, content):
        sql_content = convert_pydantic_to_sql(item=content, table=self.table)

        if sql_content:
            self.session.add(sql_content)
            await self.session.commit()
            await self.session.refresh(sql_content)

            return sql_content

    async def update(self, content_id, content):
        old_content = await self._get_by_id(content_id)

        if old_content:

            if f"content-{content_id}" in [s.decode() for s in RedisTools.get_keys()]:
                RedisTools.delete(f"content-{content_id}")

            for key, value in content.dict().items():
                setattr(old_content, key, value)
                self.session.add(old_content)
                await self.session.commit()
                await self.session.refresh(old_content)

                return old_content

    async def delete(self, content_id):
        content = await self._get_by_id(content_id)
        if content:
            if f"content-{content_id}" in [s.decode() for s in RedisTools.get_keys()]:
                RedisTools.delete(f"content-{content_id}")

            await self.session.delete(content)
            await self.session.commit()

            return True
        return False
