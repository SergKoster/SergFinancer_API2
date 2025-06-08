from pydantic import BaseModel
from typing import Optional


class CreateOperationTypeLocale(BaseModel):
    operation_type_id: int
    display_name: str
    lang: str
    

class UpdateOperationTypeLocale(BaseModel):
    operation_type_id: Optional[int] = None
    display_name: Optional[str] = None
    lang: Optional[str] = None


class GetOperationTypeLocale(BaseModel):
    id: int
    operation_type_id: int
    display_name: str
    lang: str

    
    class Config:
        from_attributes = True

