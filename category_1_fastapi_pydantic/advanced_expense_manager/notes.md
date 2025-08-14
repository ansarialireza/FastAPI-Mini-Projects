### 📓 **Project Notes**

---

## 🏷 **Project Title:**

Advanced Expense Manager API

---

## 🎯 **Project Goal:**

Build an advanced API to manage expenses with features like adding categorized expenses, validating data, generating summary reports, and exporting reports to JSON. Data will be stored in memory (a Python list) for simplicity.

---

## 🧩 **Feature List:**

* [ ] **POST** route to add a new expense
* [ ] **GET** route to list all expenses
* [ ] Filter expenses by category in the GET route
* [ ] **GET /summary/** route to calculate total expenses
* [ ] Validate `amount` > 0 using `Field(gt=0)`
* [ ] Add `date` with default `datetime.now`
* [ ] Add custom validator for `category` and future dates
* [ ] Export report to JSON file and allow download (`/export/`)
* [ ] Error handling with HTTPException for invalid inputs
* [ ] (Optional) Pagination and Sorting

---

## **Phase 1 – Planning & Design ✅**

### **API Routes Table**

| Method | Route      | Description                         | Request Body                         | Response         | Status Codes |
| ------ | ---------- | ----------------------------------- | ------------------------------------ | ---------------- | ------------ |
| POST   | /expenses/ | Add a new expense                   | {"category": "food", "amount": 50.5} | Expense          | 201, 422     |
| GET    | /expenses/ | Retrieve all expenses (with filter) | None                                 | List\[Expense]   | 200          |
| GET    | /summary/  | Get total expenses or by category   | None (use query param `category`)    | {"total": 150.0} | 200          |
| GET    | /export/   | Export all expenses as JSON file    | None                                 | File download    | 200          |

---

## 🏗 **Architecture Design**

```
advanced_expense_manager/
│
├── main.py            # Application entry point
├── models.py          # Pydantic models for Expense and Summary
├── routers/           # API route definitions
│   ├── expenses.py    # Endpoints for managing expenses
│   └── __init__.py
├── tests/             # Unit and integration tests
│   ├── test_expenses.py
│   └── __init__.py
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

---

### **📌 Notes:**

* **main.py**: Creates FastAPI app instance and includes routers.
* **models.py**: Holds request/response models (`Expense`, `Summary`).
* **routers/**: Each file contains logically grouped API endpoints.
* **tests/**: Contains automated test cases for validation and endpoints.
* **requirements.txt**: Lists dependencies (`fastapi`, `uvicorn`, `pydantic`).
* **README.md**: Explains how to install, run, and use the project.

---

### **Dependencies:**

* [x] fastapi
* [x] uvicorn
* [x] pydantic
* [x] pytest
* [x] black (for code formatting)

---

### **Edge Cases:**

* [ ] Invalid category (not in allowed list: food, transport, entertainment, etc.)
* [ ] Amount ≤ 0 (should fail validation)
* [ ] Future date for an expense (should fail validation)
* [ ] Export JSON when no expenses exist

---

## **Phase 2 – Implementation ✅**

### **Git Workflow**

* Branch name: `feature/expense-manager`
* Commit examples:

  * `feat: add Expense Pydantic model`
  * `feat: implement POST /expenses route`
  * `feat: implement GET /summary route with filtering`
  * `feat: add custom validators for category and date`
  * `feat: implement export to JSON file`

---

### **Implementation Steps**

* [x] Create `Expense` and `Summary` models with Pydantic
* [x] Add list in memory to store expenses
* [x] Implement `POST /expenses/`
* [x] Add custom validators for category and date
* [x] Implement `GET /expenses/` with category filter
* [x] Implement `GET /summary/` for total expenses
* [ ] Implement `GET /export/` for JSON download
* [ ] Add proper error handling with HTTPException
* [ ] Refactor for clean code and modularity

---

## **Phase 3 – Testing & Debugging ✅**

### **Test Cases:**

* [x] Test adding a valid expense
* [x] Test rejecting negative or zero amount
* [x] Test invalid category validation
* [ ] Test future date validation
* [x] Test filtering expenses by category
* [ ] Test exporting to JSON when expenses exist
* [ ] Test exporting when no expenses exist

---

### **Bugs & Fixes Table**

| Bug                                         | Cause                            | Fix                                  |
| ------------------------------------------- | -------------------------------- | ------------------------------------ |
| Category accepts invalid strings            | No validation implemented        | Add custom validator for category    |
| Date allows future entries                  | No date validation               | Add custom validator for future date |
| Empty JSON file when exporting with no data | Logic does not check list length | Add condition before writing file    |

---

## **Phase 4 – Deployment & Optimization ✅**

* [x] Run locally with `uvicorn main:app --reload`
* [x] Check `/docs` and `/redoc`
* [ ] Refactor into modular structure (`routers/`, `models/`)
* [ ] Add `async` for performance improvement
* [ ] Push project to GitHub
* [ ] Add `.env` for configs (future DB support)

---

## **Phase 5 – Review & Documentation ✅**

### **Retrospective:**

* **What I learned:**

  * Advanced Pydantic validations
  * Handling datetime fields in API
  * Generating reports and exporting data

* **Challenges faced:**

  * Validating allowed categories
  * Handling future dates in expense data
  * Exporting as downloadable file in FastAPI

* **Improvements for next project:**

  * Use database instead of in-memory storage
  * Implement authentication for users
  * Add pagination and sorting

---

### **README Checklist:**

* [x] Installation instructions
* [x] How to run
* [x] How to test
* [x] Short project explanation

---

## 📅 **Log Entry in learning\_log.md**

**Date:** YYYY-MM-DD
**Summary:** Completed Expense Manager API with validation, summary report, and JSON export. Learned advanced Pydantic features and response modeling.

---
