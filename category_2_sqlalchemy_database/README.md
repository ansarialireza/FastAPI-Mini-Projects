
# Category 2: SQLAlchemy and Database Integration

This category covers database integration using SQLAlchemy, including CRUD operations and table relationships.

## Projects

### simple_product_api
A basic API for managing products using SQLite.

**Key Concepts:** SQLite connection, SQLAlchemy models, CRUD operations.

**How to Run:**
```sh
cd simple_product_api
pip install -r requirements.txt
uvicorn main:app --reload
```

**Test:** Create and list products at `http://localhost:8000/products/`.

---

### intermediate_category_api
An API with product categories and One-to-Many relationships.

**Key Concepts:** One-to-Many relationships, complex queries, filtering.

**How to Run:**
```sh
cd intermediate_category_api
pip install -r requirements.txt
uvicorn main:app --reload
```

**Test:** Filter products by category.

---

### advanced_project_task_api
An API for managing projects and tasks with Many-to-Many relationships.

**Key Concepts:** Many-to-Many, Self-referencing, Alembic migrations.

**How to Run:**
```sh
cd advanced_project_task_api
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --reload
```

**Test:** Create projects and assign tasks.

---

## Requirements

- FastAPI
- SQLAlchemy
- Alembic
- SQLite

**Install dependencies:**
```sh
pip install fastapi sqlalchemy alembic
```
