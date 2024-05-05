from pydantic import BaseModel


class BaseContent(BaseModel):
    content: str
    topic_id: int

class Content(BaseContent):
    id: int

class ContentCreate(BaseContent):
    pass


class ContentUpdate(BaseContent):
    pass
