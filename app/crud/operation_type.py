from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.operation_type import OperationType
from app.schemas.operation_type import CreateOperationType, UpdateOperationType


async def get_operation_types(session: AsyncSession):
    result = await session.execute(select(OperationType))
    return result.scalars().unique().all()


async def get_operation_type(session: AsyncSession, operation_type_id: int):
    return await session.get(OperationType, operation_type_id)


async def create_operation_type(session: AsyncSession, operation_type_in: CreateOperationType):
    operation_type = OperationType(**operation_type_in.model_dump())

    session.add(operation_type)

    await session.commit()
    await session.refresh(operation_type)
    return operation_type


async def update_operation_type(session: AsyncSession, operation_type_id, operation_type_in: CreateOperationType):
    operation_type = session.get(OperationType, operation_type_id)
    for field, value in operation_type_in.model_dump(exclude_unset=True).items():
            setattr(operation_type, field, value)

    await session.commit()
    await session.refresh(operation_type)
    return operation_type


async def delete_operation_type(session: AsyncSession, operation_type_id: int):
    operation_type = await session.get(OperationType, operation_type_id)
    await session.delete(operation_type)
    
    await session.commit()
    return operation_type
