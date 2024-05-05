from fastapi import APIRouter, Depends

from anatomic.Backend.TopicContent import model
from anatomic.Backend.TopicContent.service import ContentService


router = APIRouter(tags=["Content"], prefix="/contents")


@router.get("/{topic_id}", name="Get by Topic ID")
async def get_content_by_content_id(
    topic_id: int, service: ContentService = Depends(ContentService)
):
    return await service.get_by_topic_id(topic_id)


@router.get("/")
async def get_all_content(service: ContentService = Depends(ContentService)):
    return await service.get_all()


@router.post("/")
async def create_content(
    content: model.ContentCreate, service: ContentService = Depends(ContentService)
):
    return await service.create_content(content)


@router.put("/{content_id}")
async def update_content(
    content_id,
    content: model.ContentUpdate,
    service: ContentService = Depends(ContentService),
):
    return await service.update_content(content_id, content)


@router.delete("/{content_id}")
async def delete_content(
    content_id: int, service: ContentService = Depends(ContentService)
):
    return await service.delete_content(content_id)
