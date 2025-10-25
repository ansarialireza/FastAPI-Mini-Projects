# app/routers/project.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app import schemas, crud
from app.deps import get_db

router = APIRouter(prefix="/projects", tags=["Projects"])


# ---------------------------
# Project Routes
# ---------------------------
@router.post(
    "/",
    response_model=schemas.ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_project(
    project: schemas.ProjectCreate, db: Session = Depends(get_db)
):
    return crud.ProjectCRUD(db).create(project)


@router.get(
    "/",
    response_model=List[schemas.ProjectResponse],
    status_code=status.HTTP_200_OK,
)
def get_projects(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud.ProjectCRUD(db).get_multi(skip=skip, limit=limit)


@router.get(
    "/{project_id}",
    response_model=schemas.ProjectResponse,
    status_code=status.HTTP_200_OK,
)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = crud.ProjectCRUD(db).get(project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )
    return project


@router.put(
    "/{project_id}",
    response_model=schemas.ProjectResponse,
    status_code=status.HTTP_200_OK,
)
def update_project(
    project_id: int,
    project: schemas.ProjectUpdate,
    db: Session = Depends(get_db),
):
    updated_project = crud.ProjectCRUD(db).update(project_id, project)
    if not updated_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )
    return updated_project


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    success = crud.ProjectCRUD(db).delete(project_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )
    return None
