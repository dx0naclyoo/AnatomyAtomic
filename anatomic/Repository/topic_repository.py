from typing import Any

from fastapi import Depends, HTTPException, status
from pydantic import ValidationError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from anatomic import sql_tables
from anatomic.Database.database import postgresql, RedisTools
from anatomic.Repository.base import BaseRepository
from anatomic.tools import SortedMode, is_sql_table, convert_pydantic_to_sql
from anatomic.Backend.Topic import model


class TopicRepository(BaseRepository):
    def __init__(self, session: AsyncSession = Depends(postgresql.get_session)):
        self.table = sql_tables.Topic
        self.session: AsyncSession = session

    async def get_by_slug(self, slug):  # Redis add

        if f"topic-{slug}" in [s.decode() for s in RedisTools.get_keys()]:
            print("by Slug REDIS")
            topic = RedisTools.get(f"topic-{slug}")
            dict_obj = eval("{" + topic + "}")
            return model.Topic.parse_obj(dict_obj)
        else:
            print("by ID Postgresql")
            sql = select(self.table).where(self.table.slug == slug)
            response = await self.session.execute(sql)
            topic = response.scalar()

            if topic:
                RedisTools.set(f"topic-{slug}", str(topic.__repr__()))
                return topic

    async def get(self, topic_id):

        if f"topic-{topic_id}" in [s.decode() for s in RedisTools.get_keys()]:
            print("by ID REDIS")
            topic = RedisTools.get(f"topic-{topic_id}")
            dict_obj = eval("{" + topic + "}")
            return model.Topic.parse_obj(dict_obj)
        else:
            print("by ID POSTGRESQL")
            sql = select(self.table).where(self.table.id == topic_id)
            response = await self.session.execute(sql)
            if topic := response.scalar():
                RedisTools.set(f"topic-{topic_id}", str(topic.__repr__()))
                return topic

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

        return topics

    async def create(self, topic):

        if is_sql_table(topic, self.table):
            sql_topic = topic
        else:
            sql_topic: sql_tables.Topic = convert_pydantic_to_sql(topic, self.table)

        _check = await self.get_by_slug(sql_topic.slug)

        if not _check:
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

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Topic already exist"
            )

    async def update(self, topic_id, topic):
        old_topic = await self.get(topic_id)
        if old_topic:
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
