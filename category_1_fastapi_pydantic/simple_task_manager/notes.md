# 📓 Project Notes

## 🏷 Project Title:
Simple Task Manager API (Example)

## 🎯 Project Goal:
Build a simple API to manage daily tasks with the ability to add, list, update status, and delete tasks. Data will be stored in memory (Python list) for simplicity.

## 🧩 Feature List:
- [x] GET route to list tasks
- [x] POST route to add a new task
- [x] PUT/PATCH route to update task status
- [x] DELETE route to remove a task by index
- [ ] Error handling with HTTPException
- [ ] Filtering support (`done=true/false`)

---

## Phase 1 – Planning & Design ✅
### API Routes Table
| Method | Route        | Description                   | Request Body                             | Response           | Status Codes |
|--------|--------------|--------------------------------|-------------------------------------------|--------------------|--------------|
| GET    | /tasks/      | Retrieve all tasks             | None                                      | List[Task]         | 200          |
| POST   | /tasks/      | Add a new task                 | {"title": "Buy bread", "description": ""} | Task               | 201          |
| PATCH  | /tasks/{id}  | Update task status             | {"done": true}                            | Task               | 200, 404     |
| DELETE | /tasks/{id}  | Delete task by index           | None                                      | {"msg": "deleted"} | 200, 404     |

## 🏗 Architecture Design

project_name/
│
├── main.py # Application entry point
├── models.py # Pydantic models and data schemas
├── routers/ # API route definitions (modular)
│ ├── tasks.py # Task-related endpoints
│ └── init.py
├── tests/ # Unit and integration tests
│ ├── test_tasks.py
│ └── init.py
├── requirements.txt # Project dependencies
└── README.md # Project documentation

markdown
Copy
Edit

### 📌 Notes:
- **main.py**: Creates the FastAPI app instance and includes routers.
- **models.py**: Holds request/response models using Pydantic.
- **routers/**: Each file contains logically grouped API endpoints.
- **tests/**: Contains automated test cases for each feature.
- **requirements.txt**: Lists dependencies (e.g., FastAPI, Pydantic, Uvicorn).
- **README.md**: Explains how to install, run, and use the project.


### Dependencies
- [x] fastapi
- [x] uvicorn
- [x] pydantic

### Edge Cases
- [ ] Invalid or incomplete request body
- [ ] Deleting a task that does not exist
- [ ] Updating a task that does not exist

---

## Phase 2 – Implementation ✅
### Git Workflow
- Branch name: `feature/crud`
- Commit examples:
  - `feat: add Task Pydantic model`
  - `feat: implement GET /tasks route`
  - `fix: handle invalid task index`

### Implementation Steps
- [x] Create `Task` model with Pydantic
- [x] Create in-memory `tasks` list
- [x] Implement GET `/tasks/`
- [x] Implement POST `/tasks/`
- [ ] Implement PATCH `/tasks/{id}`
- [ ] Implement DELETE `/tasks/{id}`
- [ ] Add error handling

---

## Phase 3 – Testing & Debugging ✅
### Test Cases
- [x] Test creating a new task
- [x] Test listing tasks
- [ ] Test updating task status
- [ ] Test deleting a task
- [ ] Test edge case: deleting a non-existent task

### Bugs & Fixes
| Bug                              | Cause                                  | Fix                                         |
|----------------------------------|----------------------------------------|---------------------------------------------|
| Creating a task without `title`  | Pydantic model did not enforce `title` | Set `title: str` without default value      |
| Wrong index deletion             | No index validation                    | Add `if index < len(tasks)` check           |

---

## Phase 4 – Deployment & Optimization ✅
- [x] Run locally with `uvicorn main:app --reload`
- [x] Check `/docs` and `/redoc`
- [ ] Refactor code into modular structure
- [ ] Add `async` for performance improvement
- [ ] Push to GitHub
- [ ] Add `.env` file for configs (for real projects)

---

## Phase 5 – Review & Documentation ✅
### Retrospective
- **What I learned:**
  - Working with FastAPI and Pydantic models
  - Managing in-memory data
- **Challenges faced:**
  - Index handling in delete/update operations
  - Designing a clean folder structure
- **Improvements for next project:**
  - Use a database instead of in-memory storage
  - Add more test coverage

### README Checklist
- [x] Installation instructions
- [x] How to run
- [x] How to test
- [x] Short project explanation

---

## 📅 Log Entry in `learning_log.md`
**Date:** YYYY-MM-DD  
**Summary:** Describe what was done and any problems faced
