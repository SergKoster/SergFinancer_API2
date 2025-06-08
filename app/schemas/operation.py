from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreateOperation(BaseModel):
    amount: float
    wallet_id: int
    date: datetime
    name: str
    description: Optional[str] = "-"
    operation_type_id: int


class UpdateOperation(BaseModel):
    amount: Optional[float] = None
    wallet_id: Optional[int] = None
    date: Optional[datetime] = None
    name: Optional[str] = None
    description: Optional[str] = None
    operation_type_id: Optional[int] = None


class GetOperation(BaseModel):
    id: int
    amount: float
    wallet_id: int
    date: datetime
    name: str
    description: str
    operation_type_id: int

    
    class Config:
        from_attributes = True
