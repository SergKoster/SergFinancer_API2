from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.core.db import Base

class OperationType(Base):
    __tablename__ = "operation_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)  # базовое имя, например "income", "expense"
    multiplier = Column(Float, nullable=False) 
    '''Столбец multiplier отвечает за то, как будет изменяться значение кошелька 
    при вводных данных. Например (-1) будет означать, 
    что сумму operation нужно умножить на -1, то есть это будет как расход.'''

    locales = relationship("OperationTypeLocale", back_populates="operation_type", cascade="all, delete-orphan")
