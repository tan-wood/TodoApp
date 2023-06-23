from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

from src.crud.tasks import TaskCRUD as crud
from src.auth.jwthandler import get_current_user
from src.schemas.tasks import TaskOutSchema, TaskInSchema, UpdateTask
from src.schemas.token import Status
from src.schemas.users import UserOutSchema

router = APIRouter()

@router.get(
    "/tasks",
    response_model=List[TaskOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_tasks():
    return await crud.get_tasks()

@router.get(
    "/task/{task_id}",
    response_model=TaskOutSchema,
    dependencies=[Depends(get_current_user)]
)
async def get_task(task_id: int) -> TaskOutSchema:
    try:
        return await crud.get_task(task_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Task does not exist"
        )
    
@router.post(
    "/tasks", response_model=TaskOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_task(
    task:TaskInSchema,current_user:UserOutSchema = Depends(get_current_user)
) -> TaskOutSchema:
    return await crud.create_task(task, current_user)

@router.patch(
    "/task/{task_id}",
    dependencies=[Depends(get_current_user)],
    response_model=TaskOutSchema,
    responses={404: {"model": HTTPNotFoundError}}
)
async def update_task(
    task_id: int,
    task: UpdateTask,
    current_user: UserOutSchema = Depends(get_current_user)
) -> TaskOutSchema:
    return await crud.update_task(task_id, task, current_user)

@router.delete(
    "/task/{task_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)]
)
async def delete_task(
    task_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_task(task_id, current_user)