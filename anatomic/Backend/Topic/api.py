from fastapi import APIRouter, Depends
from slugify import slugify

from anatomic.Backend.Topic import model
from anatomic.Backend.Topic.service import TopicService
from anatomic.tools import SortedMode

router = APIRouter(tags=["Topic"], prefix="/topics")


@router.get("/{identifier}")
async def get_topic_by_identifier(
    identifier: str, service: TopicService = Depends(TopicService)
):

    if identifier.isdigit():
        print("int")
        return await service.get_topic_by_id(int(identifier))
    else:
        return await service.get_topic_by_slug(identifier)


# @router.get("/{topic_id}")
# async def get_topic_by_id(topic_id: int, service: TopicService = Depends(TopicService)):
#     return await service.get_topic_by_id(topic_id)


@router.get("/")
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


@router.post("/")
async def create_topic(
    topic: model.TopicCreate, service: TopicService = Depends(TopicService)
):
    dict_create_topic = topic.dict()
    dict_create_topic["slug"] = slugify(dict_create_topic["name"])
    new_topic = model.TopicCreateBackendOnly.parse_obj(dict_create_topic)
    return await service.create(new_topic)


@router.put("/{topic_id}")
async def update_topic(
    topic_id: int,
    topic: model.TopicUpdate,
    service: TopicService = Depends(TopicService),
):
    dict_create_topic = topic.dict()
    dict_create_topic["slug"] = slugify(dict_create_topic["name"])
    new_topic = model.TopicTopicUpdateBackendOnly.parse_obj(dict_create_topic)

    return await service.update(topic_id, new_topic)


@router.delete("/{topic_id}")
async def delete_topic(topic_id: int, service: TopicService = Depends(TopicService)):
    return await service.delete(topic_id)
