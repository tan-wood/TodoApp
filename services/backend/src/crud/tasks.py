from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Tasks
from src.schemas.tasks import TaskOutSchema
import pdb

class TaskCRUD:
    async def get_tasks():
        return await TaskOutSchema.from_queryset(Tasks.all())


    async def get_task(task_id) -> TaskOutSchema:
        return await TaskOutSchema.from_queryset_single(Tasks.get(id=task_id))

    async def create_task(task, current_user) -> TaskOutSchema:
        task_dict = task.dict(exclude_unset=True)
        task_dict["user_id"] = current_user.id
        task_obj = await Tasks.create(**task_dict)
        # this taskoutschema is converting the raw task object to be what we specified it to
        # be so that we can filter the types of columns we have coming back to the user
        # it is like a DTO in C#
        return await TaskOutSchema.from_tortoise_orm(task_obj) 

    async def update_task(task_id, task, current_user)->TaskOutSchema:
        try:
            db_task = await TaskOutSchema.from_queryset_single(Tasks.get(id=task_id))
        except DoesNotExist:
            raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
        
        if db_task.user.id == current_user.id:
            await Tasks.filter(id=task_id).update(**task.dict(exclude_unset=True))
            return await TaskOutSchema.from_queryset_single(Tasks.get(id=task_id))
        
    async def delete_task(task_id, current_user):
        try:
            db_task = await TaskOutSchema.from_queryset_single(Tasks.get(id=task_id))
        except DoesNotExist:
            raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
        
        if db_task.user.id == current_user.id:
            deleted_count = await Tasks.filter(id=task_id).delete()
            if not deleted_count:
                raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
            return f"Deleted task {task_id}"
        raise HTTPException(status_code=403, detail=f"Not authorized to delete")