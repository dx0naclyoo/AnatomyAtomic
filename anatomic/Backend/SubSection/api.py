from fastapi import APIRouter, Depends

from anatomic.Backend.SubSection import model
from anatomic.Backend.SubSection.service import SubSectionService

router = APIRouter(tags=["SubSection"], prefix="/subsections")


@router.get("/{identifier}",
            name="Получение по ID или SLUG",
            description='Принимаются только значения string, например "1" или "subsection-slug" '
            )
async def get_by_identifier(
        identifier: str, service: SubSectionService = Depends(SubSectionService)):
    return await service.get_by_identifier(identifier)
        

@router.get("/")
async def get_all_subsections(
        service: SubSectionService = Depends(SubSectionService)):
    pass


@router.post("/")
async def add_subsection(
        subsection: model.SubSectionBase,
        service: SubSectionService = Depends(SubSectionService)):
    pass


@router.put("/{identifier}")
async def update_subsection(
        identifier: str,
        subsection: model.SubSectionBase,
        service: SubSectionService = Depends(SubSectionService)):
    pass


@router.delete("/{identifier}")
async def delete_subsection(
        identifier: str, service:
        SubSectionService = Depends(SubSectionService)):
    pass
