# Category 1: FastAPI and Pydantic

This category focuses on learning the basics of FastAPI and Pydantic for building APIs with data validation and serialization.

## Projects

### simple_task_manager
A basic API for managing daily tasks with CRUD operations.

**Key Concepts:** Basic routes, Pydantic models, JSON responses.

**How to Run:**
```sh
cd simple_task_manager
pip install -r requirements.txt
uvicorn main:app --reload
```

**Test:** Use Postman to send GET/POST requests to `http://localhost:8000/tasks/`.

---

### intermediate_validated_api
An enhanced task manager with advanced validation and filtering.

**Key Concepts:** Query parameters, Pydantic validation, serialization.

**How to Run:**
```sh
cd intermediate_validated_api
pip install -r requirements.txt
uvicorn main:app --reload
```

**Test:** Try filtering tasks with `?done=true`.

---

### advanced_expense_manager
An API for managing expenses with categories and reporting.

**Key Concepts:** Complex Pydantic validation, Field types, serialization.

**How to Run:**
```sh
cd advanced_expense_manager
pip install -r requirements.txt
uvicorn main:app --reload
```

**Test:** Create expenses and generate summary reports.

---

## Requirements

- FastAPI
- Pydantic
- Uvicorn

**Install dependencies:**
```sh
pip install fastapi pydantic uvicorn
```
# Category 1: FastAPI & Pydantic

- simple_task_manager
- intermediate_validated_api
- advanced_expense_manager
