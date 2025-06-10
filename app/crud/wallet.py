from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.wallet import Wallet
from app.schemas.wallet import CreateWallet, UpdateWallet


async def get_wallets(session: AsyncSession):
    result = await session.execute(select(Wallet))
    return result.scalars().unique().all()


async def get_wallet(session: AsyncSession, wallet_id: int):
    return await session.get(Wallet, wallet_id)


async def create_wallet(session: AsyncSession, wallet_in: CreateWallet):
    wallet = Wallet(**wallet_in.model_dump())

    session.add(wallet)

    await session.commit()
    await session.refresh(wallet)
    return wallet


async def update_wallet(session: AsyncSession, wallet_id, wallet_in: CreateWallet):
    wallet = session.get(Wallet, wallet_id)
    for field, value in wallet_in.model_dump(exclude_unset=True).items():
            setattr(wallet, field, value)

    await session.commit()
    await session.refresh(wallet)
    return wallet


async def delete_wallet(session: AsyncSession, wallet_id: int):
    wallet = await session.get(Wallet, wallet_id)
    await session.delete(wallet)
    
    await session.commit()
    return wallet
