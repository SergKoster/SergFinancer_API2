from pydantic import BaseModel
from typing import Optional


class CreateOperationType(BaseModel):
    name: str


class UpdateOperationType(BaseModel):
    name: Optional[str] = None


class GetOperationType(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
