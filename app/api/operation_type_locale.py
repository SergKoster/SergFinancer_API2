from fastapi import APIRouter, Depends, HTTPException, status
from app.core.db import get_async_session
from app.crud.operation_type_locale import (
    get_operation_type_locales, get_operation_type_locale, create_operation_type_locale, update_operation_type_locale, delete_operation_type_locale
)
from app.schemas.operation_type_locale import CreateOperationTypeLocale, UpdateOperationTypeLocale, GetOperationTypeLocale

router = APIRouter(prefix="/operation_type_locales", tags=["operation_type_locales"])

@router.get("/", response_model=list[GetOperationTypeLocale])
async def api_get_operation_type_locales(session = Depends(get_async_session)):
    return await get_operation_type_locales(session)


@router.get("/{operation_type_locale_id}", response_model=GetOperationTypeLocale)
async def api_get_operation_type_locale_by_id(operation_type_locale_id: int, session=Depends(get_async_session)):
    operation_type_locale = await get_operation_type_locale(session=session, operation_type_locale_id=operation_type_locale_id)
    return operation_type_locale


@router.post("/", response_model=GetOperationTypeLocale, status_code=status.HTTP_201_CREATED)
async def api_create_operation_type_locale(operation_type_locale_in: CreateOperationTypeLocale, session=Depends(get_async_session)):
    return await create_operation_type_locale(session=session, operation_type_locale_in=operation_type_locale_in)


@router.patch("/{operation_type_locale_id}", response_model=GetOperationTypeLocale)
async def api_update_operation_type_locale(operation_type_locale_id: int, operation_type_locale_in: UpdateOperationTypeLocale, session=Depends(get_async_session)):
    operation_type_locale = await update_operation_type_locale(operation_type_locale_id=operation_type_locale_id, operation_type_locale_in=operation_type_locale_in, session=session)
    return operation_type_locale


@router.delete("/{operation_type_locale_id}", response_model=GetOperationTypeLocale, status_code=status.HTTP_204_NO_CONTENT)
async def api_delete_operation_type_locale(operation_type_locale_id: int, session=Depends(get_async_session)):
    operation_type_locale = await delete_operation_type_locale(operation_type_locale_id=operation_type_locale_id, session=session)
    return 
