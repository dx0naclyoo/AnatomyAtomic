from fastapi import APIRouter, Depends

from anatomic.Backend.Topic import model
from anatomic.Backend.Topic.service import TopicService

router = APIRouter(tags=["Topic"], prefix="/topic")


@router.get("/{topic_id}")
async def get_topic_by_id(
        topic_id: int,
        service: TopicService = Depends(TopicService)
):
    return await service.get_topic_by_id(topic_id)


@router.get("/all/")
async def get_all_topic(
        limit: int = 10,
        offset: int = 0,
        sorted_mode: bool = True,
        service: TopicService = Depends(TopicService)
):
    return await service.get_all_topics()


@router.post("/create")
async def create_topic(
        topic: model.TopicCreate,
        service: TopicService = Depends(TopicService)
):
    return await service.create(topic)


@router.put("/{topic_id}/update")
async def update_topic(
        topic_id: int,
        topic: model.Topic,
        service: TopicService = Depends(TopicService)
):
    pass


@router.delete("/{topic_id}/delete")
async def delete_section(
        topic_id: int,
        service: TopicService = Depends(TopicService)
):
    pass
