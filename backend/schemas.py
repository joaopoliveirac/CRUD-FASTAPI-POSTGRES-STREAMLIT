#models vai ser sempre a REPRESENTAÇÃO do meu banco, e o meu schema sempre vai ser a representação das minhas INTERAÇÕES com o usuario
from pydantic import BaseModel, PositiveFloat, EmailStr, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    name: Optional[str] =  None
    description: Optional[str] =  None
    price: Optional[PositiveFloat] =  None
    categoria: Optional[str] =  None
    email_fornecedor: Optional[EmailStr] = None


