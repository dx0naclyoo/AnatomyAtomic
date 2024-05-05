from typing import List

from pydantic import BaseModel


class TopicBase(BaseModel):
    name: str
    keywords: List[str] = []
    subsection_id: int

class Topic(TopicBase):
    id: int
    slug: str


class TopicCreate(TopicBase):
    pass


class TopicCreateBackendOnly(TopicCreate):
    slug: str


class TopicUpdate(TopicBase):
    pass


class TopicTopicUpdateBackendOnly(TopicUpdate):
    slug: str
