from fastapi import APIRouter
from anatomic.Backend.TopicContent import model

router = APIRouter(tags=["Content"], prefix="/contents")


@router.get("/{content_id}")
async def get_content(content_id: int):
    pass


@router.get("/")
async def get_all_content():
    pass


@router.post("/")
async def create_content(content: model.ContentCreate):
    pass


@router.put("/{content_id}")
async def update_content(content_id, content: model.ContentUpdate):
    pass


@router.delete("/{content_id}")
async def delete_content(content_id: int):
    pass
