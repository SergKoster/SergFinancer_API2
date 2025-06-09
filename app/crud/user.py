from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.user import User
from app.schemas.user import CreateUser, UpdateUser


async def get_users(session: AsyncSession):
    result = await session.execute(select(User))
    return result.scalars().unique().all()


async def get_user(session: AsyncSession, user_id: int):
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, user_in: CreateUser):
    user = User(**user_in.model_dump())
    session.add(user)

    await session.commit()
    await session.refresh(user)
    return user


async def update_user(session: AsyncSession, user_id: int, user_in: UpdateUser):
    user = await session.get(User, user_id)
    for field, value in user_in.model_dump(exclude_unset=True).items():
        setattr(user, field, value)

    await session.commit()
    await session.refresh(user)
    return user


async def delete_user(session: AsyncSession, user_id: int):
    user = await session.get(User, user_id)
    await session.delete(user)
    
    await session.commit()
    return user
