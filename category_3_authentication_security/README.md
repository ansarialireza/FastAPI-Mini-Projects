
# Category 3: Authentication and Security

This category focuses on implementing authentication mechanisms in FastAPI, including Basic Auth, JWT, and API Keys.

## Projects

### simple_basic_auth
A task API with Basic Authentication.

**Key Concepts:** Basic Authentication, protected routes.

**How to Run:**
```sh
cd simple_basic_auth
pip install -r requirements.txt
uvicorn main:app --reload
```

**Test:** Use Postman with Basic Auth credentials.

---

### intermediate_jwt_auth
A task API with JWT and refresh tokens.

**Key Concepts:** JWT, access/refresh tokens, Cookie management.

**How to Run:**
```sh
cd intermediate_jwt_auth
pip install -r requirements.txt
uvicorn main:app --reload
```

**Test:** Login to get tokens and access protected routes.

---

### advanced_auth_system
A complete authentication system with signup and API Keys.

**Key Concepts:** JWT, API Key, email validation, Postman testing.

**How to Run:**
```sh
cd advanced_auth_system
pip install -r requirements.txt
uvicorn main:app --reload
```

**Test:** Register users and test API Key access.

---

## Requirements

- FastAPI
- python-jose[cryptography]
- passlib[bcrypt]
- Postman (for testing)

**Install dependencies:**
```sh
pip install fastapi python-jose[cryptography] passlib[bcrypt]
```
