from fastapi import APIRouter, Depends, HTTPException, status
from app.core.db import get_async_session
from app.crud.operation_type import (
    get_operation_types, get_operation_type, create_operation_type, update_operation_type, delete_operation_type
)
from app.schemas.operation_type import CreateOperationType, UpdateOperationType, GetOperationType

router = APIRouter(prefix="/operation_types", tags=["operation_types"])

@router.get("/", response_model=list[GetOperationType])
async def api_get_operation_types(session = Depends(get_async_session)):
    return await get_operation_types(session)


@router.get("/{operation_type_id}", response_model=GetOperationType)
async def api_get_operation_type_by_id(operation_type_id: int, session=Depends(get_async_session)):
    operation_type = await get_operation_type(session=session, operation_type_id=operation_type_id)
    return operation_type


@router.post("/", response_model=GetOperationType, status_code=status.HTTP_201_CREATED)
async def api_create_operation_type(operation_type_in: CreateOperationType, session=Depends(get_async_session)):
    return await create_operation_type(session=session, operation_type_in=operation_type_in)


@router.patch("/{operation_type_id}", response_model=GetOperationType)
async def api_update_operation_type(operation_type_id: int, operation_type_in: UpdateOperationType, session=Depends(get_async_session)):
    operation_type = await update_operation_type(operation_type_id=operation_type_id, operation_type_in=operation_type_in, session=session)
    return operation_type


@router.delete("/{operation_type_id}", response_model=GetOperationType, status_code=status.HTTP_204_NO_CONTENT)
async def api_delete_operation_type(operation_type_id: int, session=Depends(get_async_session)):
    operation_type = await delete_operation_type(operation_type_id=operation_type_id, session=session)
    return 
