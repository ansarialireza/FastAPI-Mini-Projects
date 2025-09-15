from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[TaskStatus] = TaskStatus.pending
    parent_id: Optional[int] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    parent_id: Optional[int] = None


class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# class TaskInDBBase(TaskBase):
#     id: int
#     created_at: datetime
#     updated_at: datetime


# class Config:
#     from_attributes = True


# class TaskResponse(TaskInDBBase):
#     projects: List["ProjectResponse"] = []
#     sub_tasks: List["TaskResponse"] = []


class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class ProjectResponse(ProjectBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# class ProjectInDBBase(ProjectBase):
#     id: int
#     created_at: datetime
#     updated_at: datetime

#     class Config:
#         from_attributes = True


# class ProjectResponse(ProjectInDBBase):
#     tasks: List[TaskResponse] = []
