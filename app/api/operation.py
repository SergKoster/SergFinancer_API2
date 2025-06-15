from fastapi import APIRouter, Depends, HTTPException, status
from app.core.db import get_async_session
from app.crud.operation import (
    get_operations, get_operation, create_operation, update_operation, delete_operation
)
from app.schemas.operation import CreateOperation, UpdateOperation, GetOperation

router = APIRouter(prefix="/operations", tags=["operations"])

@router.get("/", response_model=list[GetOperation])
async def api_get_operations(session = Depends(get_async_session)):
    return await get_operations(session)


@router.get("/{operation_id}", response_model=GetOperation)
async def api_get_operation_by_id(operation_id: int, session=Depends(get_async_session)):
    operation = await get_operation(session=session, operation_id=operation_id)
    return operation


@router.post("/", response_model=GetOperation, status_code=status.HTTP_201_CREATED)
async def api_create_operation(operation_in: CreateOperation, session=Depends(get_async_session)):
    return await create_operation(session=session, operation_in=operation_in)


@router.patch("/{operation_id}", response_model=GetOperation)
async def api_update_operation(operation_id: int, operation_in: UpdateOperation, session=Depends(get_async_session)):
    operation = await update_operation(operation_id=operation_id, operation_in=operation_in, session=session)
    return operation


@router.delete("/{operation_id}", response_model=GetOperation, status_code=status.HTTP_204_NO_CONTENT)
async def api_delete_operation(operation_id: int, session=Depends(get_async_session)):
    operation = await delete_operation(operation_id=operation_id, session=session)
    return 
