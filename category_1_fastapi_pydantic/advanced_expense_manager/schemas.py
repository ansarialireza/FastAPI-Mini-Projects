from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    validator,
)
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

    @field_validator("category")
    def validate_category(cls, category):
        allowed_categories = ["Food", "Transport", "Health"]
        if category.name not in allowed_categories:
            raise ValueError(
                f"Category {category.name} is not allowed. Allowed is: {allowed_categories} "
            )
        return category


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


# class Summary(BaseModel):
#     pass
