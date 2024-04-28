from fastapi import Depends

from anatomic.Repository.topic_repository import TopicRepository


class TopicService:
    def __init__(self, topic_repository: TopicRepository = Depends(TopicRepository)):
        self.topic_repository = topic_repository

    async def get_topic_by_id(self, topic_id):
        return await self.topic_repository.get(topic_id)

    async def get_all_topics(self):
        return await self.topic_repository.get_all()

    async def create(self, topic):
        return await self.topic_repository.create(topic)
