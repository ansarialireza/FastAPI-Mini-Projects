from pydantic import BaseModel, Field
from enum import Enum


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in progress"
    completed = "completed"


class TasksBase(BaseModel):
    title: str = Field(..., description="This is title for task")
    description: str
    status: TaskStatus
    # created_at: datetime
    # updated_at: datetime 


class TaskCreate(TasksBase):
    pass


class TaskResponse(TasksBase):
    task_id: int
