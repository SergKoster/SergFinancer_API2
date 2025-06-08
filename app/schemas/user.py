from pydantic import BaseModel
from typing import Optional
from app.schemas.wallet import GetWallet

# Для создания расхода (POST)
class CreateUser(BaseModel):
    username: str
    full_name: str

# Для обновления расхода (PATCH/PUT)
class UpdateUser(BaseModel):
    username: Optional[str] = None
    full_name: Optional[str] = None

# Для вывода расхода (GET) — response
class GetUser(BaseModel):
    id: int
    username: str
    full_name: str
    wallets: list[GetWallet]

    class Config:
        from_attributes = True