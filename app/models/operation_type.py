from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base

class OperationType(Base):
    __tablename__ = "operation_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)  # базовое имя, например "income", "expense"

    locales = relationship("OperationTypeLocale", back_populates="operation_type", cascade="all, delete-orphan")
