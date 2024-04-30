from typing import List

from pydantic import BaseModel

from anatomic.Backend.Topic import model


class SectionBase(BaseModel):
    name: str
    keywords: List[str] = []
    description: str


class Section(SectionBase):
    id: int
    slug: str


class SectionCreate(SectionBase):
    pass


class SectionCreateBackendOnly(SectionBase):
    slug: str


class SectionUpdate(SectionBase):
    pass
