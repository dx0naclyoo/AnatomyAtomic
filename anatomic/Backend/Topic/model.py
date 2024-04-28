from typing import List

from pydantic import BaseModel


class TopicBase(BaseModel):
    name: str
    content: str
    keywords: List[str] = []
    content: str
    section_id: int


class Topic(TopicBase):
    id: int


class TopicCreate(TopicBase):
    pass


class TopicUpdate(TopicBase):
    pass
