from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.operation_type_locale import OperationTypeLocale
from app.schemas.operation_type_locale import CreateOperationTypeLocale, UpdateOperationTypeLocale


async def get_operation_type_locales(session: AsyncSession):
    result = await session.execute(select(OperationTypeLocale))
    return result.scalars().unique().all()


async def get_operation_type_locale(session: AsyncSession, operation_type_locale_id: int):
    return await session.get(OperationTypeLocale, operation_type_locale_id)


async def create_operation_type_locale(session: AsyncSession, operation_type_locale_in: CreateOperationTypeLocale):
    operation_type_locale = OperationTypeLocale(**operation_type_locale_in.model_dump())

    session.add(operation_type_locale)

    await session.commit()
    await session.refresh(operation_type_locale)
    return operation_type_locale


async def update_operation_type_locale(session: AsyncSession, operation_type_locale_id, operation_type_locale_in: CreateOperationTypeLocale):
    operation_type_locale = session.get(OperationTypeLocale, operation_type_locale_id)
    for field, value in operation_type_locale_in.model_dump(exclude_unset=True).items():
            setattr(operation_type_locale, field, value)

    await session.commit()
    await session.refresh(operation_type_locale)
    return operation_type_locale


async def delete_operation_type_locale(session: AsyncSession, operation_type_locale_id: int):
    operation_type_locale = await session.get(OperationTypeLocale, operation_type_locale_id)
    await session.delete(operation_type_locale)
    
    await session.commit()
    return operation_type_locale
