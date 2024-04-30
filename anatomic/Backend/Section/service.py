from fastapi import Depends, HTTPException, status

from anatomic.Repository.section_repository import SectionRepository
from anatomic.tools import SortedMode


class SectionService:
    def __init__(
        self, section_repository: SectionRepository = Depends(SectionRepository)
    ):
        self.section_repository = section_repository

    async def get_section_by_slug(self, slug):
        section = await self.section_repository.get_by_slug(slug)
        if section:
            return section
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Sections not found"
            )

    async def get_section_by_id(self, section_id):
        section = await self.section_repository.get(section_id)
        if section:
            return section
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Sections not found"
            )

    async def get_all_sections(
        self, limit: int = 10, offset: int = 0, sorted_mode: SortedMode = SortedMode.ID
    ):
        sections = await self.section_repository.get_all(
            limit=limit, offset=offset, sorted_mode=sorted_mode
        )

        if sections:
            return sections
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Sections not found"
            )

    async def create_section(self, section):
        section = await self.section_repository.create(section)
        if section:
            return section
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ошибка при добавлении новой Главы. "
                       "Проверьте корректность даннных. Имена у разных секций не должно совпадать",
            )

    async def update_section(self, section_id, section):
        return await self.section_repository.update(section_id, section)

    async def delete_section(self, section_id):
        return await self.section_repository.delete(section_id)
