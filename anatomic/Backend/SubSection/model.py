from typing import List

from pydantic import BaseModel


class SubSectionBase(BaseModel):
    name: str
    description: str
    keywords: List[str] = []
    section_id: int

class SubSection(SubSectionBase):
    id: int
    slug: str


class SubSectionCreate(SubSectionBase):
    pass


class SubSectionCreateBackendOnly(SubSectionCreate):
    slug: str


class SubSectionUpdate(SubSectionBase):
    pass


class SubSectionUpdateBackendOnly(SubSectionUpdate):
    slug: str
