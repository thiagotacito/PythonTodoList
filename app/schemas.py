from pydantic import BaseModel
from typing import Optional

# Schema for creating a new task
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

#send back data
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

    class Config:
        orm_mode = True