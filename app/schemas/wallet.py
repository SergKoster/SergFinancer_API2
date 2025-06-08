from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from decimal import Decimal

# Для создания расхода (POST)
class CreateWallet(BaseModel):
    name: str
    balance: Decimal

    user_id: int
    currency_id: int

# Для обновления расхода (PATCH/PUT)
class UpdateWallet(BaseModel):
    name: Optional[str] = None
    balance: Optional[Decimal] = None

    user_id: Optional[int] = None
    currency_id: Optional[int] = None

# Для вывода расхода (GET) — response
class GetWallet(BaseModel):
    id: int
    name: str
    balance: Decimal

    user_id: int
    currency_id: int

    date_of_create: datetime

    class Config:
        from_attributes = True
