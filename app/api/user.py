from fastapi import APIRouter, Depends, HTTPException, status
from app.core.db import get_async_session
from app.crud.user import (
    get_users, get_user, create_user, update_user, delete_user
)
from app.schemas.user import CreateUser, UpdateUser, GetUser

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[GetUser])
async def api_get_users(session = Depends(get_async_session)):
    return await get_users(session)


@router.get("/{user_id}", response_model=GetUser)
async def api_get_user_by_id(user_id: int, session=Depends(get_async_session)):
    user = await get_user(session=session, user_id=user_id)
    return user


@router.post("/", response_model=GetUser, status_code=status.HTTP_201_CREATED)
async def api_create_user(user_in: CreateUser, session=Depends(get_async_session)):
    return await create_user(session=session, user_in=user_in)


@router.patch("/{user_id}", response_model=GetUser)
async def api_update_user(user_id: int, user_in: UpdateUser, session=Depends(get_async_session)):
    user = await update_user(user_id=user_id, user_in=user_in, session=session)
    return user


@router.delete("/{user_id}", response_model=GetUser, status_code=status.HTTP_204_NO_CONTENT)
async def api_delete_user(user_id: int, session=Depends(get_async_session)):
    user = await delete_user(user_id=user_id, session=session)
    return 
