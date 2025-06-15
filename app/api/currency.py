from fastapi import APIRouter, Depends, HTTPException, status
from app.core.db import get_async_session
from app.crud.currency import (
    get_currencys, get_currency, create_currency, update_currency, delete_currency
)
from app.schemas.currency import CreateCurrency, UpdateCurrency, GetCurrency

router = APIRouter(prefix="/currencys", tags=["currencys"])

@router.get("/", response_model=list[GetCurrency])
async def api_get_currencys(session = Depends(get_async_session)):
    return await get_currencys(session)


@router.get("/{currency_id}", response_model=GetCurrency)
async def api_get_currency_by_id(currency_id: int, session=Depends(get_async_session)):
    currency = await get_currency(session=session, currency_id=currency_id)
    return currency


@router.post("/", response_model=GetCurrency, status_code=status.HTTP_201_CREATED)
async def api_create_currency(currency_in: CreateCurrency, session=Depends(get_async_session)):
    return await create_currency(session=session, currency_in=currency_in)


@router.patch("/{currency_id}", response_model=GetCurrency)
async def api_update_currency(currency_id: int, currency_in: UpdateCurrency, session=Depends(get_async_session)):
    currency = await update_currency(currency_id=currency_id, currency_in=currency_in, session=session)
    return currency


@router.delete("/{currency_id}", response_model=GetCurrency, status_code=status.HTTP_204_NO_CONTENT)
async def api_delete_currency(currency_id: int, session=Depends(get_async_session)):
    currency = await delete_currency(currency_id=currency_id, session=session)
    return 
