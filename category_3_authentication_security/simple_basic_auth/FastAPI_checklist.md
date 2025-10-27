# ✅ FastAPI Project General Checklist

A comprehensive, battle-tested checklist for initializing, building, testing, securing, and deploying scalable FastAPI applications.  
Follow this blueprint for clean architecture, best practices, and maintainability.  

*Inspired by modern Python standards (PEP 8/621), async patterns, and production-grade setups.*  
*Pro Tip: Bookmark this and tick off items progressively—start with Setup, then iterate through Development phases.*

---

## 🧱 1. Project Initialization & Setup

- [ ] **Create and activate a virtual environment**  
  *Use `venv` or `conda` for isolation:*  
  ```bash
  python -m venv .venv
  source .venv/bin/activate  # On Windows: .venv\Scripts\activate
  ```

- [ ] **Initialize Git repository**  
  ```bash
  git init
  git add .
  git commit -m "Initial commit: FastAPI project skeleton"
  ```

- [ ] **Add `.gitignore`**  
  *Include: `__pycache__`, `.venv`, `.env`, `*.pyc`, `node_modules` (if frontend), `.DS_Store`.*  
  Use [gitignore.io](https://gitignore.io) for Python/FastAPI templates.

- [ ] **Install core dependencies**  
  ```bash
  pip install fastapi uvicorn[standard] python-dotenv pydantic-settings
  ```

- [ ] **Set up dependency management**  
  *Choose `pip` + `requirements.txt`, or advanced: `poetry` or `pipenv`.*  
  ```bash
  # For Poetry
  poetry init
  poetry add fastapi uvicorn
  ```

- [ ] **Establish clean directory structure**  
  *Modular, scalable layout following domain-driven design:*  
  ```
  my_project/
  ├── app/                          # Main application package
  │   ├── __init__.py
  │   ├── main.py                   # FastAPI app instance & routers
  │   ├── core/                     # App-wide configs & utilities
  │   │   ├── __init__.py
  │   │   ├── config.py             # Settings loader
  │   │   ├── security.py           # Auth/JWT helpers
  │   │   └── exceptions.py         # Custom exceptions
  │   ├── models/                   # ORM models (SQLAlchemy/Tortoise)
  │   │   ├── __init__.py
  │   │   └── user.py
  │   ├── schemas/                  # Pydantic validation models
  │   │   ├── __init__.py
  │   │   ├── base.py               # Base schemas
  │   │   └── user.py               # User-specific schemas
  │   ├── api/                      # API layer (routers & endpoints)
  │   │   ├── __init__.py
  │   │   ├── deps.py               # Shared dependencies
  │   │   └── v1/                   # Versioned API
  │   │       ├── __init__.py
  │   │       ├── api.py            # Main API router
  │   │       └── endpoints/        # Feature-based routes
  │   │           ├── __init__.py
  │   │           ├── users.py
  │   │           └── auth.py
  │   ├── crud/                     # Data access layer (repositories)
  │   │   ├── __init__.py
  │   │   ├── base.py               # Base CRUD
  │   │   └── user.py
  │   ├── db/                       # Database connections & sessions
  │   │   ├── __init__.py
  │   │   ├── base.py               # Engine & session maker
  │   │   └── session.py            # Dependency for DB sessions
  │   └── utils/                    # Reusable helpers
  │       ├── __init__.py
  │       ├── logger.py             # Structured logging
  │       └── helpers.py            # Misc utilities (e.g., email, pagination)
  ├── tests/                        # Comprehensive test suite
  │   ├── __init__.py
  │   ├── conftest.py               # Pytest fixtures
  │   ├── unit/                     # Unit tests
  │   │   └── test_crud.py
  │   ├── integration/              # Integration tests
  │   │   └── test_users.py
  │   └── e2e/                      # End-to-end tests
  │       └── test_auth_flow.py
  ├── migrations/                   # DB migrations (Alembic)
  │   ├── versions/
  │   ├── env.py
  │   └── script.py.mako
  ├── docs/                         # API & project docs (optional MkDocs)
  │   └── index.md
  ├── .env.example                  # Template for env vars
  ├── .env                          # Local secrets (gitignored)
  ├── requirements.txt              # Or pyproject.toml for Poetry
  ├── pyproject.toml                # Build & lint config (if using Poetry/Black)
  ├── Dockerfile                    # Containerization
  ├── docker-compose.yml            # Local dev/prod stack
  ├── .dockerignore
  ├── README.md                     # Project overview & quickstart
  └── LICENSE                       # MIT/Apache/etc.
  ```

---

## ⚙️ 2. Configuration & Environment Management

- [ ] **Leverage environment variables** for all secrets/configs  
  *Never hardcode—use `python-dotenv` for loading.*

- [ ] **Create `.env` and `.env.example`**  
  *Example vars: `DATABASE_URL`, `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`.*

- [ ] **Implement config loader** in `app/core/config.py`  
  *Use `pydantic-settings` for validation:*  
  ```python
  from pydantic_settings import BaseSettings
  from typing import Optional

  class Settings(BaseSettings):
      app_name: str = "FastAPI Project"
      version: str = "0.1.0"
      database_url: str
      secret_key: str
      debug: bool = False
      allowed_hosts: list[str] = ["*"]
      log_level: str = "INFO"

      class Config:
          env_file = ".env"
          env_file_encoding = "utf-8"

  settings = Settings()
  ```

- [ ] **Support multi-environment configs**  
  *Dev/prod/testing via profiles (e.g., `DEBUG=True` for dev).*

- [ ] **Validate configs on startup**  
  *Raise `ValueError` for missing required vars.*

---

## 🗄️ 3. Database & Data Layer

- [ ] **Select ORM/Driver**  
  *SQLAlchemy (sync/async), Tortoise-ORM (async-first), or raw asyncpg.*

- [ ] **Configure connection** in `app/db/base.py` & `session.py`  
  *Async support:*  
  ```python
  from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
  from sqlalchemy.orm import sessionmaker

  engine = create_async_engine(settings.database_url)
  AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
  ```

- [ ] **Define models** in `app/models/`  
  *Inherit from `Base` with relationships & indexes.*

- [ ] **Set up migrations** with Alembic  
  ```bash
  pip install alembic
  alembic init migrations
  # Edit alembic.ini & env.py for async if needed
  alembic revision --autogenerate -m "Initial migration"
  alembic upgrade head
  ```

- [ ] **Implement CRUD** in `app/crud/`  
  *Repository pattern: `get()`, `create()`, `update()`, `delete()`.*

- [ ] **Test connectivity**  
  *Run a simple query in a startup event.*

---

## 🧩 4. Schemas, Validation & Serialization

- [ ] **Define Pydantic schemas** in `app/schemas/`  
  *Base, Create, Update, Read (with exclusions for passwords).*

- [ ] **Separate concerns**  
  *`UserCreate` (input), `UserOut` (output), `UserInDB` (internal).*

- [ ] **Add validators & constraints**  
  ```python
  from pydantic import validator, EmailStr, Field

  class UserCreate(BaseModel):
      email: EmailStr
      password: str = Field(..., min_length=8)
      # Custom validator
      @validator('password')
      def validate_password(cls, v):
          if not any(c.isupper() for c in v):
              raise ValueError('Password must contain uppercase letter')
          return v
  ```

- [ ] **Enable schema reuse**  
  *Import across layers; use `Union` for flexible responses.*

---

## 🌐 5. API Routing & Controllers

- [ ] **Modularize with APIRouter**  
  *One router per feature (e.g., `users_router = APIRouter(tags=["users"])`).*

- [ ] **Organize endpoints** in `app/api/v1/endpoints/`  
  *RESTful: GET/POST/PUT/DELETE with pagination.*

- [ ] **Mount routers** in `app/api/v1/api.py` & `main.py`  
  ```python
  from fastapi import FastAPI
  from app.api.v1.api import api_router

  app = FastAPI(title=settings.app_name, version=settings.version)
  app.include_router(api_router, prefix="/api/v1")
  ```

- [ ] **Handle exceptions globally** in `app/core/exceptions.py`  
  *Custom `HTTPException` for 404, 422, etc.*

- [ ] **Add startup/shutdown events**  
  *e.g., DB connect on startup.*

---

## 🔐 6. Authentication & Authorization

- [ ] **Choose scheme**: JWT (recommended) or OAuth2  
  *Install: `pip install python-jose[cryptography] passlib[bcrypt]`.  

- [ ] **Hash passwords** with `passlib`  
  ```python
  from passlib.context import CryptContext
  pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
  ```

- [ ] **Build dependencies** in `app/core/security.py`  
  *`create_access_token()`, `get_current_user()`.*

- [ ] **Secure routes**  
  *`@router.post(..., dependencies=[Depends(get_current_user)])`.*

- [ ] **Add RBAC/ABAC** if complex  
  *Roles in DB, check via `user.role in allowed_roles`.*

- [ ] **Implement refresh tokens** for long sessions.

---

## 🧪 7. Testing Suite

- [ ] **Install tools**  
  ```bash
  pip install pytest pytest-asyncio httpx pytest-cov
  ```

- [ ] **Configure `conftest.py`**  
  *Fixtures: `client = TestClient(app)`, `override_db`.*

- [ ] **Write tests** in `tests/`  
  *Unit (CRUD), Integration (API calls), E2E (full flows).*  
  *Use `httpx.AsyncClient` for async:*  
  ```python
  @pytest.mark.asyncio
  async def test_create_user(client: AsyncClient):
      response = await client.post("/api/v1/users/", json={"email": "test@example.com", "password": "Test123!"})
      assert response.status_code == 201
  ```

- [ ] **Aim for 80%+ coverage**  
  *Run: `pytest --cov=app --cov-report=html`.*

- [ ] **Mock externalities** (e.g., `pytest-mock` for DB/externals).

---

## 🧰 8. Utilities, Middlewares & Logging

- [ ] **Set up logging** in `app/utils/logger.py`  
  *Use `loguru` or stdlib with JSON format for production.*

- [ ] **Add middlewares**  
  *CORS: `CORSMiddleware(allow_origins=settings.allowed_hosts)`.*  
  *Rate limiting: `slowapi`.*

- [ ] **Custom error handling**  
  *Middleware for tracing & Sentry integration.*

- [ ] **Background tasks**  
  *`BackgroundTasks` for emails/notifications.*

- [ ] **Reusable utils**  
  *Pagination, email sender, file upload helpers.*

---

## 📜 9. Documentation & API Specs

- [ ] **Enable auto-docs**  
  *Access `/docs` (Swagger) & `/redoc`—add `description`, `tags`, `responses`.*

- [ ] **Enhance with examples**  
  *`response_model=UserOut, response_description="User created successfully"`.*

- [ ] **Version APIs**  
  *`/api/v1`, `/api/v2` for breaking changes.*

- [ ] **Generate OpenAPI spec**  
  *Export YAML/JSON; use for Postman/Insomnia collections.*

- [ ] **Project README**  
  *Include setup, run commands, architecture diagram (Mermaid).*

---

## 📦 10. Dependency Injection & Management

- [ ] **Freeze deps**  
  ```bash
  pip freeze > requirements.txt  # Or poetry lock
  ```

- [ ] **Use `Depends()`** everywhere  
  *DB session, current user, etc.*

- [ ] **Isolate layers**  
  *No direct imports between CRUD/API—use DI.*

- [ ] **Lint & format**  
  *Add `black`, `isort`, `flake8` to `pyproject.toml`.*

---

## 🐳 11. Containerization & Orchestration

- [ ] **Craft `Dockerfile`**  
  *Multi-stage:*  
  ```dockerfile
  # Build stage
  FROM python:3.12-slim AS builder
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt

  # Runtime stage
  FROM python:3.12-slim
  WORKDIR /app
  COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
  COPY . .
  CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```

- [ ] **Compose stack** in `docker-compose.yml`  
  *App + Postgres + Redis.*  

- [ ] **Add `.dockerignore`**  
  *Exclude `.git`, `tests`, `__pycache__`.*

- [ ] **Local test**  
  ```bash
  docker compose up --build
  ```

---

## 🔒 12. Security Hardening

- [ ] **Enforce HTTPS**  
  *Certbot or cloud provider (e.g., AWS ALB).*

- [ ] **Input/Output validation**  
  *Pydantic + OWASP guidelines (prevent SQLi, XSS).*

- [ ] **Suppress tracebacks**  
  *`debug=False` in prod; use custom exception handlers.*

- [ ] **Secure JWT**  
  *Strong `SECRET_KEY` (env var), short expiry (15min).*

- [ ] **CORS & Headers**  
  *Strict origins; add `SecurityHeadersMiddleware`.*

- [ ] **Rate limiting & Auditing**  
  *`slowapi`; log sensitive actions.*

- [ ] **Dependency scans**  
  *`pip-audit` or Snyk regularly.*

---

## 📈 13. Performance Optimization & Monitoring

- [ ] **Async everything**  
  *I/O ops (DB, HTTP) with `async def`.*

- [ ] **Profiling tools**  
  *`cProfile` or `py-spy`; load test with `locust`.*

- [ ] **Caching layer**  
  *Redis via `fastapi-cache2` for frequent queries.*

- [ ] **DB optimizations**  
  *Indexes, connection pooling, query limits.*

- [ ] **Metrics & Logs**  
  *Prometheus exporter; ELK stack or Datadog.*

---

## 🌍 14. Deployment & CI/CD

- [ ] **Production server**  
  ```bash
  gunicorn -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 app.main:app
  ```

- [ ] **Reverse proxy**  
  *Nginx/Apache for static files & load balancing.*

- [ ] **Health checks**  
  *`/health` endpoint; Docker probes.*

- [ ] **CI/CD pipeline**  
  *GitHub Actions: lint/test/build/deploy on push.*  
  *Example: Test on PR, deploy to staging on merge.*

- [ ] **Cloud-agnostic**  
  *Heroku/Vercel for simple; AWS ECS/K8s for scale.*

- [ ] **Secrets management**  
  *Vault, AWS SSM—never in repo.*

---

## 🧾 15. Ongoing Maintenance & Best Practices

- [ ] **Pre-deploy checklist**  
  *Run `pytest`, `black .`, `alembic upgrade head`.*

- [ ] **Dependency hygiene**  
  *Weekly `pip list --outdated`; auto-update via Dependabot.*

- [ ] **Error monitoring**  
  *Sentry for exceptions; fix top issues first.*

- [ ] **Docs evolution**  
  *Update on every feature; changelog in README.*

- [ ] **Backups & DR**  
  *Automated DB dumps (pg_dump); test restores.*

- [ ] **Code reviews & Refactors**  
  *Pair programming; refactor high-complexity modules.*

- [ ] **Security audits**  
  *Quarterly: OWASP ZAP scans, code reviews.*

---

**🚀 Quickstart Command:**  
```bash
git clone <repo> && cd my_project && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && uvicorn app.main:app --reload
```

**Author:** Alireza Ansari (Enhanced by Grok)  
**Template Version:** v2.0 (Updated Oct 2025)  
*Feedback? Fork & contribute on GitHub!*