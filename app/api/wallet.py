from fastapi import APIRouter, Depends, HTTPException, status
from app.core.db import get_async_session
from app.crud.wallet import (
    get_wallets, get_wallet, create_wallet, update_wallet, delete_wallet
)
from app.schemas.wallet import CreateWallet, UpdateWallet, GetWallet

router = APIRouter(prefix="/wallets", tags=["wallets"])

@router.get("/", response_model=list[GetWallet])
async def api_get_wallets(session = Depends(get_async_session)):
    return await get_wallets(session)


@router.get("/{wallet_id}", response_model=GetWallet)
async def api_get_wallet_by_id(wallet_id: int, session=Depends(get_async_session)):
    wallet = await get_wallet(session=session, wallet_id=wallet_id)
    return wallet


@router.post("/", response_model=GetWallet, status_code=status.HTTP_201_CREATED)
async def api_create_wallet(wallet_in: CreateWallet, session=Depends(get_async_session)):
    return await create_wallet(session=session, wallet_in=wallet_in)


@router.patch("/{wallet_id}", response_model=GetWallet)
async def api_update_wallet(wallet_id: int, wallet_in: UpdateWallet, session=Depends(get_async_session)):
    wallet = await update_wallet(wallet_id=wallet_id, wallet_in=wallet_in, session=session)
    return wallet


@router.delete("/{wallet_id}", response_model=GetWallet, status_code=status.HTTP_204_NO_CONTENT)
async def api_delete_wallet(wallet_id: int, session=Depends(get_async_session)):
    wallet = await delete_wallet(wallet_id=wallet_id, session=session)
    return 
