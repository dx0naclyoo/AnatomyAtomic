from fastapi import APIRouter, Depends, Request

from anatomic.Backend.Section import model
from anatomic.Backend.Section.service import SectionService
from anatomic.tools import SortedMode

router = APIRouter(tags=["Section"], prefix="/sections")


@router.get(
    "/{section_id}", response_model=model.Section, name="section:get_by_id"
)
async def get_section_by_id(
    section_id: int, service: SectionService = Depends(SectionService)
):
    return await service.get_section_by_id(section_id)


@router.get(
    "/",
    description="""
    CRUD Операция - получение всех Секций из БД. 
    limit - Число записей, что вернётся, max = 100.
    offset - смещение записей, пример offset=10: response: item_id - ..... 10, 11, 12, 13.
    group_by - Ещё НЕ РЕАЛИЗОВАНО, групировка по параметрам.
    """,
)
async def get_all_section(
    request: Request,
    limit: int = 10,
    offset: int = 0,
    sorted_mode: SortedMode = SortedMode.ID,
    service: SectionService = Depends(SectionService),
):
    if limit > 100:
        limit = 100
    return await service.get_all_sections(
        limit=limit, offset=offset, sorted_mode=sorted_mode
    )


@router.post("/")
async def create_section(
    section: model.SectionCreate, service: SectionService = Depends(SectionService)
):
    return await service.create_section(section)


@router.put("/{section_id}")
async def update_section(
    section_id: int,
    section: model.SectionUpdate,
    service: SectionService = Depends(SectionService),
):
    return await service.update_section(section_id, section)


@router.delete("/{section_id}")
async def delete_section(
    section_id: int, service: SectionService = Depends(SectionService)
):
    return await service.delete_section(section_id)
