
# Category 6: Docker, CI/CD, and Production

This category covers containerization, CI/CD pipelines, and deploying FastAPI apps to production.

## Projects

### simple_docker_todo
A Todo App containerized with Docker and PostgreSQL.

**Key Concepts:** Docker, docker-compose, PostgreSQL, Alembic migrations.

**How to Run:**
```sh
cd simple_docker_todo
pip install -r requirements.txt
docker-compose up --build
```

**Test:** Access `http://localhost:8000` and verify database connection.

---

### intermediate_celery_redis
A Todo App with Celery and Redis for background tasks.

**Key Concepts:** Celery, Redis, APScheduler, Flower monitoring.

**How to Run:**
```sh
cd intermediate_celery_redis
pip install -r requirements.txt
docker-compose up --build
```

**Test:** Monitor tasks with Flower at `http://localhost:5555`.

---

### advanced_cicd_production
A Todo App with CI/CD and error monitoring.

**Key Concepts:** CI/CD with GitHub Actions, Sentry, Load Testing with Locust.

**How to Run:**
```sh
cd advanced_cicd_production
pip install -r requirements.txt
docker-compose up --build
```

**Test:** Push to GitHub to trigger CI/CD and check Sentry for errors.

---

## Requirements

- Docker
- Docker Compose
- PostgreSQL
- Redis
- Celery
- Locust
- Sentry SDK

**Install dependencies:**
```sh
pip install fastapi sqlalchemy alembic celery redis locust sentry-sdk
```
