# Simple Product API

A basic API for managing products using SQLite and SQLAlchemy.

## Key Concepts
- SQLite connection
- SQLAlchemy models
- CRUD operations

## How to Run
```sh
pip install -r requirements.txt
uvicorn main:app --reload
```

## Test
Create and list products at `http://localhost:8000/products/`.
