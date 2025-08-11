# Advanced Project Task API

An API for managing projects and tasks with Many-to-Many relationships using SQLAlchemy and Alembic.

## Key Concepts
- Many-to-Many
- Self-referencing
- Alembic migrations

## How to Run
```sh
pip install -r requirements.txt
alembic upgrade head
uvicorn main:app --reload
```

## Test
Create projects and assign tasks.
