from fastapi import Depends, status, HTTPException

from anatomic.Repository.topic_repository import TopicRepository
from anatomic.tools import SortedMode


class TopicService:
    def __init__(self, topic_repository: TopicRepository = Depends(TopicRepository)):
        self.topic_repository = topic_repository

    async def get_by_identifier(self, identifier):
        if identifier.isdigit():
            topic = await self.topic_repository.get_by_id(int(identifier))
        else:
            topic = await self.topic_repository.get_by_slug(identifier)
        if topic:
            return topic
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Topics not found"
            )

    async def get_all_topics(
        self,
        subsection_id: int = None,
        limit: int = 10,
        offset: int = 0,
        sorted_mode: SortedMode = SortedMode.ID,
    ):
        topics = await self.topic_repository.get_all(
            limit=limit,
            offset=offset,
            sorted_mode=sorted_mode,
            subsection_id=subsection_id,
        )

        return topics

    async def create(self, topic):
        topic = await self.topic_repository.create(topic)

        if not topic:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Topic not created. Возникла ошибка, такая тема уже существует или введены не валидные данные"
            )
        
        else:
            return topic
        
    async def update(self, identifier, topic):
        old_topic = await self.get_by_identifier(identifier)

        if old_topic:
            return await self.topic_repository.update(old_topic.id, topic)

    async def delete(self, identifier):
        topic_for_delete = await self.get_by_identifier(identifier)

        if topic_for_delete:
            return await self.topic_repository.delete(topic_for_delete.id)
