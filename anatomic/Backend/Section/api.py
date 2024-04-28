from fastapi import APIRouter, Depends

from anatomic.Backend.Section import model
from anatomic.Backend.Section.service import SectionService

router = APIRouter(tags=["Section"], prefix="/section")


@router.get("/")
async def get_section_by_id(
        service: SectionService = Depends(SectionService)
):
    pass




