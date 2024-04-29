from fastapi import Depends, status, HTTPException

from anatomic.Repository.topic_repository import TopicRepository
from anatomic.tools import SortedMode


class TopicService:
    def __init__(self, topic_repository: TopicRepository = Depends(TopicRepository)):
        self.topic_repository = topic_repository

    async def get_topic_by_slug(self, slug):
        topic = await self.topic_repository.get_by_slug(slug)
        if topic:
            return topic
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Topics not found"
            )

    async def get_topic_by_id(self, topic_id):
        topic = await self.topic_repository.get(topic_id)
        if topic:
            return topic
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Topics not found"
            )

    async def get_all_topics(
        self,
        section_id: int = None,
        limit: int = 10,
        offset: int = 0,
        sorted_mode: SortedMode = SortedMode.ID,
    ):
        topics = await self.topic_repository.get_all(
            limit=limit, offset=offset, sorted_mode=sorted_mode, section_id=section_id
        )

        if topics:
            return topics
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Topics not found"
            )

    async def create(self, topic):
        return await self.topic_repository.create(topic)

    async def update(self, topic_id, topic):
        return await self.topic_repository.update(topic_id, topic)

    async def delete(self, topic_id):
        return await self.topic_repository.delete(topic_id)
