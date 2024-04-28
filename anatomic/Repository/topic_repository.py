from typing import Any

from fastapi import Depends, HTTPException, status
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from anatomic import sql_tables
from anatomic.Database.database import postgresql
from anatomic.Repository.base import BaseRepository
from anatomic.tools import SortedMode


class TopicRepository(BaseRepository):
    def __init__(self, session: AsyncSession = Depends(postgresql.get_session)):
        self.table = sql_tables.Topic
        self.session: AsyncSession = session

    @staticmethod
    def convert_to_sql(topic: Any) -> sql_tables.Topic:
        if isinstance(topic, sql_tables.Topic):
            return topic
        else:
            try:
                return sql_tables.Topic(**topic.dict())
            except ValidationError as e:
                raise e

    @staticmethod
    def is_sql_table(topic: Any) -> bool:
        if isinstance(topic, sql_tables.Topic):
            return True
        else:
            return False

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
        limit: int = 10,
        offset: int = 0,
        sorted_mode: SortedMode = SortedMode.ID,
    ):
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
        if self.is_sql_table(topic):
            sql_topic = topic
        else:
            sql_topic = self.convert_to_sql(topic)

        self.session.add(sql_topic)
        await self.session.commit()
        await self.session.refresh(sql_topic)
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
