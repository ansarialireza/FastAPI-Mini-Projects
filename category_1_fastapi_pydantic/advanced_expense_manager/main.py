from fastapi import FastAPI, status
from schemas import ExpenseResponse, ExpenseCreate

app = FastAPI()


expenses_db = []


def generate_unique_expense_id(db: list) -> int:
    if not db:
        return 1
    return max(db, key=lambda x: x["expense_id"])["task_id"] + 1


app.get(
    "/expenses/",
    status_code=status.HTTP_200_OK,
    response_model=ExpenseResponse,
)


async def list_expenses():
    return expenses_db


app.post(
    "/expenses/",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
)


async def add_expense(expense: ExpenseCreate):
    expenses_db.append(
        {
            "id": generate_unique_expense_id(expenses_db),
            "amount": expense.amount,
            "category": expense.category,
        }
    )
