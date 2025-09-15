from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas


# ---------------------------
# Project CRUD
# ---------------------------
class ProjectCRUD:
    def __init__(self, db: Session):
        self.db = db

    def get(self, project_id: int) -> Optional[models.Project]:
        return (
            self.db.query(models.Project)
            .filter(models.Project.id == project_id)
            .first()
        )

    def get_multi(
        self, skip: int = 0, limit: int = 100
    ) -> List[models.Project]:
        return self.db.query(models.Project).offset(skip).limit(limit).all()

    def create(self, project: schemas.ProjectCreate) -> models.Project:
        db_project = models.Project(**project.model_dump())
        self.db.add(db_project)
        self.db.commit()
        self.db.refresh(db_project)
        return db_project

    def update(
        self, project_id: int, project: schemas.ProjectUpdate
    ) -> Optional[models.Project]:
        db_project = self.get(project_id)
        if not db_project:
            return None
        update_data = project.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_project, key, value)
        self.db.commit()
        self.db.refresh(db_project)
        return db_project

    def delete(self, project_id: int) -> bool:
        db_project = self.get(project_id)
        if not db_project:
            return False
        self.db.delete(db_project)
        self.db.commit()
        return True


# ---------------------------
# Task CRUD
# ---------------------------
class TaskCRUD:
    def __init__(self, db: Session):
        self.db = db

    def get(self, task_id: int) -> Optional[models.Task]:
        return (
            self.db.query(models.Task)
            .filter(models.Task.id == task_id)
            .first()
        )

    def get_multi(self, skip: int = 0, limit: int = 100) -> List[models.Task]:
        return self.db.query(models.Task).offset(skip).limit(limit).all()

    def create(self, task: schemas.TaskCreate) -> models.Task:
        db_task = models.Task(**task.model_dump())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def update(
        self, task_id: int, task: schemas.TaskUpdate
    ) -> Optional[models.Task]:
        db_task = self.get(task_id)
        if not db_task:
            return None
        update_data = task.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_task, key, value)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def delete(self, task_id: int) -> bool:
        db_task = self.get(task_id)
        if not db_task:
            return False
        self.db.delete(db_task)
        self.db.commit()
        return True

    def assign_to_project(
        self, task_id: int, project_id: int
    ) -> Optional[models.Task]:
        db_task = self.get(task_id)
        db_project = (
            self.db.query(models.Project)
            .filter(models.Project.id == project_id)
            .first()
        )
        if not db_task or not db_project:
            return None
        db_task.projects.append(db_project)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task
