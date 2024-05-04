from fastapi import Depends, HTTPException, status

from anatomic.Backend.SubSection import model
from anatomic.Repository.subsection_repository import SubSectionRepository


class SubSectionService:
    def __init__(self, subsection_repository: SubSectionRepository = Depends(SubSectionRepository)):
        self.subsection_repository = subsection_repository

    async def get_by_identifier(self, identifier: str):
        if identifier.isdigit():
            subsection = await self.subsection_repository.get_by_id(int(identifier))
        else:
            subsection = await self.subsection_repository.get_by_slug(identifier)

        if not subsection:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="SubSection not found")

        return subsection

    async def get_all(
        self,
        limit: int = 10,
        offset: int = 0,
        section_id: int = None,
    ):
        return await self.subsection_repository.get_all(limit=limit, offset=offset, section_id=section_id)

    async def create(self, subsection: model.SubSectionCreateBackendOnly):
        response = await self.subsection_repository.create(subsection)
        if response:
            return response
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="SubSection not created. Возникла ошибка, такая подсекция уже существует или введены не валидные данные")

    async def update(
        self, identifier: str, subsection_new: model.SubSectionUpdateBackendOnly
    ):

        if identifier.isdigit():
            old_subsection = await self.subsection_repository._get_by_id(int(identifier))
        else:
            old_subsection = await self.subsection_repository._get_by_slug(int(identifier))

        updated_subsection = await self.subsection_repository.update(
            old_subsection=old_subsection, subsection_new=subsection_new
        )

        if updated_subsection:
            return updated_subsection
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="SubSection not updated")

    async def delete(self, subsection_id):
        pass
