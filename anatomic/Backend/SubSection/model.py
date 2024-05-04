from typing import List

from pydantic import BaseModel


class SubSectionBase(BaseModel):
    name: str
    description: str
    eywords: List[str] = []


class SubSection(SubSectionBase):
    id: int
    section_id: int


class SubSectionCreate(SubSectionBase):
    slug: str


class SubSectionUpdate(SubSectionBase):
    slug: str
