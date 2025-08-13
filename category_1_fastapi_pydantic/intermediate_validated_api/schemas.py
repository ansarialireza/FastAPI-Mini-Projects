from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in progress"
    completed = "completed"


class TasksBase(BaseModel):
    title: str = Field(
        ..., min_length=3, max_length=35, description="This is title for task"
    )
    priority: int = Field(
        ..., gt=1, le=5, description="Priority of task (1-5)"
    )
    description: Optional[str] = Field(
        default=None,
        min_length=10,
        max_length=255,
        description="This is descriptiion for task",
    )
    status: TaskStatus = Field(..., description=" This is status for task")


class TaskCreate(TasksBase):
    pass


class TaskUpdate(TasksBase):
    title: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=35,
        description="This is title for task",
    )
    priority: Optional[int] = Field(
        default=None, gt=1, le=5, description="Priority of task (1-5)"
    )
    description: Optional[str] = Field(
        default=None,
        min_length=10,
        max_length=255,
        description="This is descriptiion for task",
    )
    status: Optional[TaskStatus] = Field(
        default=None, description=" This is status for task"
    )


class TaskResponse(TasksBase):
    task_id: int
