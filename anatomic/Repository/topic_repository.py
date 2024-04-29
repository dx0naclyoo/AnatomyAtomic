from typing import Any

from fastapi import Depends, HTTPException, status
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from anatomic import sql_tables
from anatomic.Database.database import postgresql
from anatomic.Repository.base import BaseRepository
from anatomic.tools import SortedMode, is_sql_table, convert_pydantic_to_sql


class TopicRepository(BaseRepository):
    def __init__(self, session: AsyncSession = Depends(postgresql.get_session)):
        self.table = sql_tables.Topic
        self.session: AsyncSession = session

    async def get_by_slug(self, slug):
        sql = select(self.table).where(self.table.slug == slug)
        response = await self.session.execute(sql)
        if topic := response.scalar():
            return topic
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found"
            )

    async def get(self, topic_id):
        sql = select(self.table).where(self.table.id == topic_id)
        response = await self.session.execute(sql)
        if topic := response.scalar():
            return topic
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Topic not found"
            )

    async def get_all(
        self,
        section_id: int = None,
        limit: int = 10,
        offset: int = 0,
        sorted_mode: SortedMode = SortedMode.ID,
    ):
        if section_id:
            sql = (
                select(self.table)
                .limit(limit)
                .offset(offset)
                .filter(self.table.section_id == section_id)
            )
        else:
            sql = select(sql_tables.Topic).limit(limit).offset(offset)

        response = await self.session.execute(sql)
        topics = response.scalars().all()

        if topics:
            return topics
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Topics not found"
            )

    async def create(self, topic):
        if is_sql_table(topic, self.table):
            sql_topic = topic
        else:
            sql_topic = convert_pydantic_to_sql(topic, self.table)

        try:
            self.session.add(sql_topic)
            await self.session.commit()
            await self.session.refresh(sql_topic)
        except IntegrityError as error:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ошибка при добавлении новой темы. "
                "Проверьте корректность даннных, возможно такой Секции не сущетсвует",
            )
        return sql_topic

    async def update(self, topic_id, topic):
        old_topic = await self.get(topic_id)

        for key, value in topic.dict().items():
            setattr(old_topic, key, value)

        await self.session.commit()
        await self.session.refresh(old_topic)

        return old_topic

    async def delete(self, topic_id):

        topic = await self.get(topic_id)

        if topic:
            await self.session.delete(topic)
            await self.session.commit()
            return True
        else:
            return False
