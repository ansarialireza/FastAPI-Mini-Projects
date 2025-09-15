# app/routers/task.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app import schemas, crud
from app.deps import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# ---------------------------
# Task Routes
# ---------------------------
@router.post(
    "/",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.TaskCRUD(db).create(task)


@router.get(
    "/",
    response_model=List[schemas.TaskResponse],
    status_code=status.HTTP_200_OK,
)
def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.TaskCRUD(db).get_multi(skip=skip, limit=limit)


@router.get(
    "/{task_id}",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_200_OK,
)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.TaskCRUD(db).get(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return task


@router.put(
    "/{task_id}",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_200_OK,
)
def update_task(
    task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)
):
    updated_task = crud.TaskCRUD(db).update(task_id, task)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return updated_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    success = crud.TaskCRUD(db).delete(task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return None


@router.post(
    "/{task_id}/assign/{project_id}",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_200_OK,
)
def assign_task_to_project(
    task_id: int, project_id: int, db: Session = Depends(get_db)
):
    task = crud.TaskCRUD(db).assign_to_project(task_id, project_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task or Project not found",
        )
    return task
