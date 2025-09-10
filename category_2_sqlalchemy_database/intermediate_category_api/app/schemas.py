from pydantic import BaseModel, Field
from typing import Optional


class CategoryBase(BaseModel):
    name: str = Field(..., max_length=40)
    description: str = Field(..., max_length=200)


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=40)
    description: Optional[str] = Field(None, max_length=40)


class CategoryResponse(CategoryBase):
    id: int = Field(..., ge=0)

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str = Field(..., max_length=40)
    description: str = Field(..., max_length=200)
    price: float = Field(..., ge=0)
    quantity: int = Field(..., ge=0)
    category_id: int = Field(..., ge=0)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    name: Optional[str] = Field(None, max_length=40)
    description: Optional[str] = Field(None, max_length=200)
    price: Optional[float] = Field(None, ge=0)
    quantity: Optional[int] = Field(None, ge=0)
    category_id: Optional[int] = Field(None, ge=0)


class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True
