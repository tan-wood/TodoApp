from typing import Optional
from datetime import date

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Tasks

TaskInSchema = pydantic_model_creator(
    Tasks, name="TaskIn", exclude=["user_id"], exclude_readonly=True
)
TaskOutSchema = pydantic_model_creator(
    Tasks, name="TaskOut", exclude=[
        "modified_at", "user.password", "user.created_at", "user.modified_at"    
        ]
)

class UpdateTask(BaseModel):
    title: Optional[str]
    comments: Optional[str]
    priority_level: Optional[int]
    due_date: Optional[date]