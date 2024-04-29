from fastapi import Depends

from anatomic.Repository.section_repository import SectionRepository
from anatomic.tools import SortedMode


class SectionService:
    def __init__(
        self, section_repository: SectionRepository = Depends(SectionRepository)
    ):
        self.section_repository = section_repository

    async def get_section_by_slug(self, slug):
        return await self.section_repository.get_by_slug(slug)

    async def get_section_by_id(self, section_id):
        return await self.section_repository.get(section_id)

    async def get_all_sections(
        self, limit: int = 10, offset: int = 0, sorted_mode: SortedMode = SortedMode.ID
    ):
        return await self.section_repository.get_all(
            limit=limit, offset=offset, sorted_mode=sorted_mode
        )

    async def create_section(self, section):
        return await self.section_repository.create(section)

    async def update_section(self, section_id, section):
        return await self.section_repository.update(section_id, section)

    async def delete_section(self, section_id):
        return await self.section_repository.delete(section_id)
