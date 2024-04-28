from typing import List

from pydantic import BaseModel

from anatomic.Backend.Topic import model


class SectionBase(BaseModel):
    name: str


class Section(SectionBase):
    id: int
    topic_list: List["model.Topic"] = []
    keywords: List[str] = []


class SectionCreate(SectionBase):
    pass
