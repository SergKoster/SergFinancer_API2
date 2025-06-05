from sqlalchemy import Column, Integer, Numeric, ForeignKey, DateTime, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.db import Base

class Operation(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Numeric(18, 2), nullable=False)
    wallet_id = Column(Integer, ForeignKey("wallets.id", ondelete="CASCADE"), nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    operation_type_id = Column(Integer, ForeignKey("operation_types.id", ondelete="CASCADE"), nullable=False)

    wallet = relationship("Wallet", back_populates="operations")
