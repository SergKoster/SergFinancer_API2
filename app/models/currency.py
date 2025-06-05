from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base

class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    symbol = Column(String, nullable=False)   # например, "₽", "$", "€"
    code = Column(String(3), unique=True, nullable=False)  # ISO код, например "RUB", "USD"

    wallets = relationship("Wallet", back_populates="currency", cascade="all, delete-orphan")
