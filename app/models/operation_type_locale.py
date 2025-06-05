from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base

class OperationTypeLocale(Base):
    __tablename__ = "operation_types_locales"

    id = Column(Integer, primary_key=True, index=True)
    operation_type_id = Column(Integer, ForeignKey("operation_types.id", ondelete="CASCADE"), nullable=False)
    display_name = Column(String, nullable=False)  # например "Доход", "Расход"
    lang = Column(String(2), nullable=False)       # ISO code: "ru", "en" и т. д.

    operation_type = relationship("OperationType", back_populates="locales")
