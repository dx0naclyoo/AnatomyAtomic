from fastapi import Depends

from anatomic.Repository.subsection_repository import SubSectionRepository


class SubSectionService:
    def __init__(self, topic_repository: SubSectionRepository = Depends(SubSectionRepository)):
        self.topic_repository = topic_repository

    async def get_by_identifier(self, identifier: str):
        if identifier.isdigit():
            return await self.topic_repository.get_by_id(int(identifier))
        else:
            return await self.topic_repository.get_by_slug(identifier)

    async def create(self, subsection):
        pass

    async def update(self, subsection, subsection_id):
        pass

    async def delete(self, subsection_id):
        pass
