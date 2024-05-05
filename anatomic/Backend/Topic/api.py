from fastapi import APIRouter, Depends
from slugify import slugify

from anatomic.Backend.Topic import model
from anatomic.Backend.Topic.service import TopicService
from anatomic.tools import SortedMode

router = APIRouter(tags=["Topic"], prefix="/topics")


@router.get(
    "/{identifier}",
    name="Получение по ID или SLUG",
    description='Принимаются только значения string, например "1" или "subsection-slug" ',
)
async def get_topic_by_identifier(
    identifier: str, service: TopicService = Depends(TopicService)
):
    return await service.get_by_identifier(identifier)


@router.get("/")
async def get_all_topic(
    limit: int = 10,
    offset: int = 0,
    sorted_mode: SortedMode = SortedMode.ID,
    subsection_id: int = None,
    service: TopicService = Depends(TopicService),
):
    if limit > 100:
        limit = 100

    return await service.get_all_topics(
        limit=limit, offset=offset, subsection_id=subsection_id, sorted_mode=sorted_mode
    )


@router.post("/")
async def create_topic(
    topic: model.TopicCreate, service: TopicService = Depends(TopicService)
):
    dict_create_topic = topic.dict()
    dict_create_topic["slug"] = slugify(dict_create_topic["name"])
    new_topic = model.TopicCreateBackendOnly.parse_obj(dict_create_topic)
    print(new_topic)
    return await service.create(new_topic)


@router.put("/{identifier}")
async def update_topic(
    identifier: str,
    topic: model.TopicUpdate,
    service: TopicService = Depends(TopicService),
):
    dict_create_topic = topic.dict()
    dict_create_topic["slug"] = slugify(dict_create_topic["name"])
    new_topic = model.TopicTopicUpdateBackendOnly.parse_obj(dict_create_topic)

    return await service.update(identifier, new_topic)


@router.delete("/{identifier}")
async def delete_topic(identifier: str, service: TopicService = Depends(TopicService)):
    return await service.delete(identifier)
