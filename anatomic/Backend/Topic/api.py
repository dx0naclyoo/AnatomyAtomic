from fastapi import APIRouter, Depends

from anatomic.Backend.Topic import model
from anatomic.Backend.Topic.service import TopicService
from anatomic.tools import SortedMode

router = APIRouter(tags=["Topic"])


@router.get("/topics/{topic_id}")
async def get_topic_by_id(topic_id: int, service: TopicService = Depends(TopicService)):
    return await service.get_topic_by_id(topic_id)


@router.get("/topics")
async def get_all_topic(
    limit: int = 10,
    offset: int = 0,
    sorted_mode: SortedMode = SortedMode.ID,
    section_id: int = None,
    service: TopicService = Depends(TopicService),
):
    if limit > 100:
        limit = 100

    return await service.get_all_topics(
        limit=limit,
        offset=offset,
        sorted_mode=sorted_mode,
        section_id=section_id,
    )


@router.post("/topic/")
async def create_topic(
    topic: model.TopicCreate, service: TopicService = Depends(TopicService)
):
    return await service.create(topic)


@router.put("/topic/{topic_id}")
async def update_topic(
    topic_id: int,
    topic: model.TopicUpdate,
    service: TopicService = Depends(TopicService),
):
    return await service.update(topic_id, topic)


@router.delete("/topic/{topic_id}")
async def delete_topic(topic_id: int, service: TopicService = Depends(TopicService)):
    return await service.delete(topic_id)
