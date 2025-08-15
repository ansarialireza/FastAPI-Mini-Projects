from fastapi import FastAPI, status, Body, Query, HTTPException, Response
from typing import Annotated, Optional, List
from schemas import TaskCreate, TaskResponse, TaskStatus, TaskUpdate

app = FastAPI()


tasks_db = []


def generate_unique_task_id(db: list) -> int:
    if not db:
        return 1
    return max(db, key=lambda x: x["task_id"])["task_id"] + 1


@app.get(
    "/tasks/",
    status_code=status.HTTP_200_OK,
    response_model=List[TaskResponse],
    response_model_exclude={
        "description",
    },
)
async def list_tasks(
    status: Annotated[Optional[TaskStatus], Query] = None,
    priority: Annotated[
        Optional[int],
        Query(ge=1, le=5, description="This is priority for task."),
    ] = None,
):
    status_db = []
    priority_db = []
    if status:
        status_db = [item for item in tasks_db if item["status"] == status]
    if priority:
        priority_db = [
            item for item in tasks_db if item["priority"] == priority
        ]
    if (not priority) and (not status):
        return [TaskResponse(**item) for item in tasks_db]
    return status_db + priority_db


@app.get(
    "/tasks/{task_id}",
    response_model=TaskResponse,
    response_model_exclude=["description"],  # type: ignore
    status_code=status.HTTP_200_OK,
)
async def get_task(task_id: int):
    if task_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
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
    task_id = generate_unique_task_id(tasks_db)
    new_task = {
        "task_id": task_id,
        "title": task.title,
        "priority": task.priority,
        "description": task.description,
        "status": task.status,
    }
    tasks_db.append(new_task)
    return new_task


@app.patch(
    "/tasks/{task_id}",
    response_model=TaskResponse,
    response_model_exclude_unset=True,
    # response_model_exclude_none=True,
)
async def update_task(task_id: int, task: Annotated[TaskUpdate, Body()]):
    if task_id <= 0:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Task must be positive integer",
        )
    for item in tasks_db:
        if item["task_id"] == task_id:
            if task.title is not None:
                item["title"] = task.title
            if task.priority is not None:
                item["priority"] = task.priority
            if task.description is not None:
                item["description"] = task.description
            if task.status is not None:
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
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
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
