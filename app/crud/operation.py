from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.operation import Operation
from app.models.wallet import Wallet
from app.models.operation_type import OperationType
from app.schemas.operation import CreateOperation, UpdateOperation


async def get_operations(session: AsyncSession):
    result = await session.execute(select(Operation))
    return result.scalars().unique().all()


async def get_operations_by_wallet(session: AsyncSession, wallet_id: int):
    result = await session.execute(
        select(Operation).where(Operation.wallet_id == wallet_id)
    )
    return result.scalars().all()


async def get_operation(session: AsyncSession, operation_id: int):
    return await session.get(Operation, operation_id)


async def create_operation(session: AsyncSession, operation_in: CreateOperation):
    operation = Operation(**operation_in.model_dump())
    await add_to_wallet(session, operation)
    
    await session.add(operation)
    await session.commit()
    await session.refresh(operation)
    return operation
    




# Бизнес-логика

async def add_to_wallet(session: AsyncSession, operation: Operation):
    """Получаем operation и wallet_id, ищем multiplier через operation.operation_type_id
    Потом берём amount из operation и прибавляем amount * multiplier к балансу кошелька"""
    wallet = await session.get(Wallet, operation.wallet_id)
    operation_type = await session.get(OperationType, operation.operation_type_id)
    multiplier = operation_type.multiplier
    amount = operation.amount

    wallet.balance += amount * multiplier


