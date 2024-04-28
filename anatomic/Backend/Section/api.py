from fastapi import APIRouter, Depends

from anatomic.Backend.Section import model
from anatomic.Backend.Section.service import SectionService
from anatomic.tools import SortedMode

router = APIRouter(tags=["Section"], prefix="/section")


@router.get("/{section_id}")
async def get_section_by_id(
    section_id: int, service: SectionService = Depends(SectionService)
):
    pass


@router.get("/all")
async def get_all_section(
    limit: int = 10,
    offset: int = 0,
    sorted_mode: SortedMode = SortedMode.ID,
    service: SectionService = Depends(SectionService),
):
    pass


@router.post("/create")
async def create_section(
    section: model.Section, service: SectionService = Depends(SectionService)
):
    pass


@router.put("/{section_id}/update")
async def update_section(
    section_id: int,
    section: model.Section,
    service: SectionService = Depends(SectionService),
):
    pass


@router.delete("/{section_id}/delete")
async def delete_section(
    section_id: int, service: SectionService = Depends(SectionService)
):
    pass
