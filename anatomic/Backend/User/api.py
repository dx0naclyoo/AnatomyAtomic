from fastapi import APIRouter, Depends

from anatomic.Backend.User import model
from anatomic.Backend.User.service import UserService

router = APIRouter(tags=["User"], prefix="/user")


@router.get("/{user_id}")
async def get_by_id(user_id: int, service: UserService = Depends(UserService)):
    user = await service.get_user(user_id)
    return user


@router.post("/create", response_model=model.User)
async def create_user(
    user: model.UserRegister, service: UserService = Depends(UserService)
):
    user = await service.add_user(user)
    return user
