from pydantic import BaseModel
from typing import Optional


class CreateCurrency(BaseModel):
    name: str
    symbol: str
    code: str


class UpdateCurrency(BaseModel):
    name: Optional[str] = None
    symbol: Optional[str] = None
    code: Optional[str] = None


class GetCurrency(BaseModel):
    id: int
    name: str
    symbol: str
    code: str

    
    class Config:
        from_attributes = True
