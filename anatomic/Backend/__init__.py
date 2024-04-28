from fastapi import APIRouter
from .User.api import router as user_router
from .Section.api import router as section_router
from .Topic.api import router as topic_router

router = APIRouter(prefix="/api/v1")
router.include_router(user_router)
router.include_router(section_router)
router.include_router(topic_router)

