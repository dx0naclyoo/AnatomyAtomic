from typing import List

from pydantic import BaseModel


class TopicBase(BaseModel):
    name: str
    content: str
    keywords: List[str] = []


class Topic(TopicBase):
    id: int


class TopicCreate(TopicBase):
    content: str
    section_id: int
