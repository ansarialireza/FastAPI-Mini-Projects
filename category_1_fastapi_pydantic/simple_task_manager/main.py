from fastapi import FastAPI, status, Body, HTTPException, Response
from typing import Annotated
from schemas import TaskCreate, TaskResponse


app = FastAPI()


tasks_db = []


def genereate_unique_task_id(db: list) -> int:
    if not db:
        return 0
    return max(db, key=lambda x: x["task_id"])["task_id"] + 1


@app.get("/tasks/", status_code=status.HTTP_200_OK)
async def list_tasks():
    return tasks_db


@app.get(
    "/tasks/{task_id}",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK,
)
async def get_task(task_id: int):
    if task_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task ID must be positive integer",
        )

    for task in tasks_db:
        if task["task_id"] == task_id:
            return TaskResponse(**task)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Item not found !"
    )


@app.post(
    "/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED
)
async def add_task(task: Annotated[TaskCreate, Body()]):
    task_id = genereate_unique_task_id(tasks_db)
    new_task = {
        "task_id": task_id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
    }
    tasks_db.append(new_task)
    return new_task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task: Annotated[TaskCreate, Body()]):
    if task_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task must be positive integer",
        )
    for item in tasks_db:
        if item["task_id"] == task_id:
            item["title"] = task.title
            item["description"] = task.description
            item["status"] = task.status
            return TaskResponse(**item)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with id {task_id} not found !",
    )


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    if task_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task must be positive integer",
        )
    for item in tasks_db:
        if item["task_id"] == task_id:
            tasks_db.remove(item)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with id {task_id} not found !",
    )
