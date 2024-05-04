from fastapi import APIRouter, Depends
from slugify import slugify

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
    limit: int = 10,
    offset: int = 0,
    section_id: int = None,
    service: SubSectionService = Depends(SubSectionService),
):
    if limit > 100:
        limit = 100
    return await service.get_all(limit=limit, offset=offset, section_id=section_id)


@router.post("/")
async def add_subsection(
        subsection: model.SubSectionCreate,
        service: SubSectionService = Depends(SubSectionService)):
    
    dict_subsection = subsection.dict()
    dict_subsection["slug"] = slugify(dict_subsection["name"])

    new_model = model.SubSectionCreateBackendOnly.parse_obj(dict_subsection)
    return await service.create(new_model) 

@router.put("/{identifier}")
async def update_subsection(
        identifier: str,
        subsection: model.SubSectionUpdate,
        service: SubSectionService = Depends(SubSectionService)):

    dict_subsection = subsection.dict()
    dict_subsection["slug"] = slugify(dict_subsection["name"])

    new_model = model.SubSectionUpdateBackendOnly.parse_obj(dict_subsection)

    return await service.update(identifier, new_model)

@router.delete("/{identifier}")
async def delete_subsection(
        identifier: str, service:
        SubSectionService = Depends(SubSectionService)):
    return await service.delete(identifier)
