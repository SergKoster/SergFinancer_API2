from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.currency import Currency
from app.schemas.currency import CreateCurrency, UpdateCurrency


async def get_currencys(session: AsyncSession):
    result = await session.execute(select(Currency))
    return result.scalars().unique().all()


async def get_currency(session: AsyncSession, currency_id: int):
    return await session.get(Currency, currency_id)


async def create_currency(session: AsyncSession, currency_in: CreateCurrency):
    currency = Currency(**currency_in.model_dump())
    session.add(currency)

    await session.commit()
    await session.refresh(currency)
    return currency


async def update_currency(session: AsyncSession, currency_id: int, currency_in: UpdateCurrency):
    currency = await session.get(Currency, currency_id)
    for field, value in currency_in.model_dump(exclude_unset=True).items():
        setattr(currency, field, value)

    await session.commit()
    await session.refresh(currency)
    return currency


async def delete_currency(session: AsyncSession, currency_id: int):
    currency = await session.get(Currency, currency_id)
    await session.delete(currency)
    
    await session.commit()
    return currency
