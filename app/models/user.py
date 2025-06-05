from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_username = Column(String, unique=True, index=True, nullable=False)
    telegram_id = Column(Integer, unique=True, index=True, nullable=False)

    wallets = relationship("Wallet", back_populates="owner", cascade="all, delete-orphan")
