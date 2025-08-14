from pydantic import BaseModel, Field
from typing import Optional


class Category(BaseModel):
    id: int = Field(..., description="Unique identifier for the category")
    name: str = Field(..., max_length=50, description="Name of category")
    description: Optional[str] = Field(
        None, max_length=255, description="Description about Category"
    )


class ExpensesBase(BaseModel):
    title: str = Field(..., max_length=100, description="Title of expense")
    amount: float = Field(
        ..., gt=0, description="Amount must be grater then 0"
    )
    category: Category


class ExpenseCreate(ExpensesBase):
    pass


class ExpenseUpdate(ExpensesBase):
    title: Optional[str] = Field(
        None, max_length=100, description="Title of expense"
    )
    amount: Optional[float] = Field(
        None, gt=0, description="Amount must be grater then 0"
    )
    category: Optional[Category] = Field(
        None, description="category of expenses"
    )


class ExpenseResponse(ExpensesBase):
    id: int = Field(..., description="Unique identifier for the expense")


class Summary(BaseModel):
    pass
