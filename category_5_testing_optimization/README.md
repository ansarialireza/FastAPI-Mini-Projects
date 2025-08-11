
# Category 5: Testing and Optimization

This category focuses on writing tests, handling errors, and optimizing FastAPI applications.

## Projects

### simple_pytest_tasks
Writing basic tests for a task API with Pytest.

**Key Concepts:** Pytest, fixtures, testing CRUD operations.

**How to Run:**
```sh
cd simple_pytest_tasks
pip install -r requirements.txt
pytest
```

**Test:** Run tests to verify API functionality.

---

### intermediate_error_background
A task API with custom error handling and background tasks.

**Key Concepts:** Custom exception handlers, background tasks, PEP8.

**How to Run:**
```sh
cd intermediate_error_background
pip install -r requirements.txt
uvicorn main:app --reload
pytest
```

**Test:** Trigger errors and verify logs.

---

### advanced_cache_testing
A task API with caching and advanced tests.

**Key Concepts:** Memory caching, advanced fixtures, performance testing.

**How to Run:**
```sh
cd advanced_cache_testing
pip install -r requirements.txt
uvicorn main:app --reload
pytest
```

**Test:** Verify cache functionality with tests.

---

## Requirements

- FastAPI
- Pytest
- Black
- Flake8

**Install dependencies:**
```sh
pip install fastapi pytest black flake8
```
