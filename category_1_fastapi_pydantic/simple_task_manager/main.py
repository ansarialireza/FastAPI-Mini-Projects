from fastapi import FastAPI, Body, status
from typing import Annotated
from schemas import TaskCreate, TaskResponse


app = FastAPI()


tasks_db = []


@app.get("/tasks/")
async def list_tasks():
    return tasks_db


@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    pass


@app.post("/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def add_task(task: Annotated[TaskCreate, Body()]):
    new_task = {
        "task_id": 1,
        "title": task.title,
        "description": task.description,
        "status": task.status,
    }
    tasks_db.append(new_task)
    return new_task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int):
    pass


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    pass
