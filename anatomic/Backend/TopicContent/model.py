from pydantic import BaseModel


class BaseContent(BaseModel):
    content: str


class Content(BaseContent):
    id: int


class ContentCreate(BaseContent):
    pass


class ContentUpdate(BaseContent):
    pass
