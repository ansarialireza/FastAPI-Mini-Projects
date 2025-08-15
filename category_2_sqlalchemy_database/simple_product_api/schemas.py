from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str = Field(..., max_length=50, description="Product name")
    price: float = Field(..., max_length=20, description="Product price")


class ProductCreate(ProductBase):
    pass


class ProductRespinse(ProductBase):
    id: int = Field(..., description="Product Id")
