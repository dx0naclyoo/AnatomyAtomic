from typing import List

from pydantic import BaseModel

from anatomic.Backend.Topic import model


class SectionBase(BaseModel):
    name: str
    keywords: List[str] = []


class Section(SectionBase):
    id: int


class SectionCreate(SectionBase):
    pass


class SectionUpdate(SectionBase):
    pass
