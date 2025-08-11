
# Category 4: Project Management and Middleware

This category covers building structured APIs with proper layouts and middleware for CORS and data handling.

## Projects

### simple_todo_app
A Todo App with standard project structure.

**Key Concepts:** Standard layout, Pydantic schemas, CRUD operations.

**How to Run:**
```sh
cd simple_todo_app
pip install -r requirements.txt
uvicorn main:app --reload
```

**Test:** Create and list tasks at `http://localhost:8000/tasks/`.

---

### intermediate_cors_random_data
A Todo App with CORS and random data generation.

**Key Concepts:** CORS middleware, random data, filtering.

**How to Run:**
```sh
cd intermediate_cors_random_data
pip install -r requirements.txt
uvicorn main:app --reload
```

**Test:** Access from a frontend with CORS enabled.

---

### advanced_multilingual_todo
A multilingual Todo App with advanced filtering.

**Key Concepts:** Multilingual support, complex filters, custom middleware.

**How to Run:**
```sh
cd advanced_multilingual_todo
pip install -r requirements.txt
uvicorn main:app --reload
```

**Test:** Switch languages with `?lang=fa`.

---

## Requirements

- FastAPI
- Pydantic
- Faker (for random data)

**Install dependencies:**
```sh
pip install fastapi pydantic faker
```
