from fastapi import Depends, status, HTTPException

from anatomic.Repository.topic_content_repository import TopicContentRepository
from anatomic.tools import SortedMode


class ContentService:
    def __init__(
        self,
        content_repository: TopicContentRepository = Depends(TopicContentRepository),
    ):
        self.content_repository = content_repository

    async def get_by_id(self, content_id):
        content = await self.content_repository.get(content_id)
        if content:
            return content
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Content not found"
            )

    async def get_all(self):
        return await self.content_repository.get_all()

    async def create_content(self, content):
        content = await self.content_repository.create(content)
        if content:
            return content
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Не удалось создать",
            )

    async def update_content(self, content_id, content):
        old_content = await self.get_by_id(content_id)
        
        if content:
            return await self.content_repository.update(old_content.id, content)

    async def delete_content(self, content_id):
        content_for_delete = await self.get_by_id(content_id)
        
        if content_for_delete:
            return await self.content_repository.delete(content_for_delete.id)
