from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.database.models import Users
from src.schemas.users import UserOutSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(user) -> UserOutSchema:
    # we are setting the password given to us to the newly encrypted password
    user.password = pwd_context.encrypt(user.password)

    try:
        # because it is a tortoise model, then it has this create method that we
        # can use

        '''
        In the code **user.dict(exclude_unset=True), the double asterisks (**) are 
        used to perform keyword argument unpacking in Python.

        The user object is expected to be a dictionary-like object that 
        has a dict() method. By using **user.dict(exclude_unset=True), 
        it means that the dictionary returned by user.dict(exclude_unset=True) 
        will be unpacked as keyword arguments.
        '''
        user_obj = await Users.create(**user.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(status_code=401, detail=f"Sorry, that username already exits.")
    
    return await UserOutSchema.from_tortoise_orm(user_obj)


async def delete_user(user_id, current_user):
    try:
        db_user = await UserOutSchema.from_queryset_single(Users.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    # if the user that is going to be deleted is not the current user, then they will
    # not be able to delete the user
    if db_user.id == current_user.id:
        deleted_count = await Users.filter(id=user_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"User {user_id} not found")
        return f"Deleted user {user_id}"
    
    raise HTTPException(status_code=403, detail=f"Not authorized to delete")