from typing import List

from pydantic import BaseModel


class TopicBase(BaseModel):
    name: str
    content: str


class Topic(TopicBase):
    id: int
    keywords: List[str] = []


class TopicCreate(TopicBase):
    content: str
