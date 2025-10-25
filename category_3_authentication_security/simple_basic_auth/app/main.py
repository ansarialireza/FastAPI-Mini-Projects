# app/main.py
from fastapi import FastAPI
from app.routers import task, project
from app.database import Base, engine

# ---------------------------
# Create database tables
# ---------------------------
Base.metadata.create_all(bind=engine)

# ---------------------------
# Initialize FastAPI app
# ---------------------------
app = FastAPI(
    title="Project & Task Management API",
    description="API for managing projects and tasks with SQLAlchemy, Pydantic, and FastAPI",
    version="1.0.0",
)

# ---------------------------
# Include Routers
# ---------------------------
app.include_router(project.router)
app.include_router(task.router)


# ---------------------------
# Root endpoint
# ---------------------------
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to Project & Task Management API"}
