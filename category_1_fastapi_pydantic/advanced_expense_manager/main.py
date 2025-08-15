from fastapi import FastAPI, status, Body, Query
from schemas import ExpenseResponse, ExpenseCreate
from typing import Annotated, List, Optional
from fastapi.responses import StreamingResponse
import json


app = FastAPI()


expenses_db = []


def generate_unique_expense_id(db: list) -> int:
    if not db:
        return 1
    return max(db, key=lambda x: x["id"])["id"] + 1


@app.get(
    "/expenses/",
    status_code=status.HTTP_200_OK,
    response_model=List[ExpenseResponse],
)
async def list_expenses(
    category: Annotated[Optional[str], Query()] = None,
):
    if category:
        return [
            item for item in expenses_db if item["category"].name == category
        ]

    return expenses_db


@app.post(
    "/expenses/",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
)
async def add_expense(expense: Annotated[ExpenseCreate, Body()]):
    new_expense = {
        "id": generate_unique_expense_id(expenses_db),
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
    }
    expenses_db.append(new_expense)
    return ExpenseResponse(**new_expense)


@app.get("/summary/", status_code=status.HTTP_200_OK)
async def get_expenses_summary(
    category: Annotated[Optional[str], Query] = None,
):
    if category:
        total_expenses = sum(
            [
                item["amount"]
                for item in expenses_db
                if item["category"].name == category
            ]
        )
        return total_expenses
    total_expenses = sum([item["amount"] for item in expenses_db])
    return {"total": total_expenses}


@app.get(
    "/export/",
    response_model=List[ExpenseResponse],
    status_code=status.HTTP_200_OK,
)
async def export_expenses():
    expenses_json = json.dumps(
        [ExpenseResponse(**item).model_dump() for item in expenses_db],
        indent=2,
    )
    return StreamingResponse(
        content=iter([expenses_json]),
        media_type="application/json",
        headers={"Content-Disposition": "attachment; filename=expenses.json"},
    )
