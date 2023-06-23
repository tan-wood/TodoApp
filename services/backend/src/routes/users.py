from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from tortoise.contrib.fastapi import HTTPNotFoundError

import src.crud.users as crud
from src.auth.users import validate_user
from src.schemas.token import Status
from src.schemas.users import UserInSchema, UserOutSchema

from src.auth.jwthandler import (
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

router = APIRouter()

@router.post("/register", response_model=UserOutSchema)
async def create_user(user: UserInSchema)->UserOutSchema:
    return await crud.create_user(user)

@router.post("/login")
async def login(user: OAuth2PasswordRequestForm = Depends()):
    user = await validate_user(user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token= create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)
    content = {"message": "You've successfully logged in. Welcome back!"}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False # TODO: WE have to set this to true in production when we deal with HTTPS things
    )
    '''
    The name of the cookie is Authorization with a value of Bearer {token}, with token being the actual token. It expires after 1800 seconds (30 minutes).
    httponly is set to True for security purposes so that client-side scripts won't be able to access the cookie. This helps prevent Cross Site Scripting (XSS) attacks.
    With samesite set to Lax, the browser only sends cookies on some HTTP requests. This helps prevent Cross Site Request Forgery (CSRF) attacks.
    Finally, secure is set to False since we'll be testing locally, without HTTPS. Make sure to set this to True in production.
    '''

    return response

@router.get(
    "/users/whoami", response_model=UserOutSchema,dependencies=[Depends(get_current_user)]
)
async def read_users_me(current_user: UserOutSchema = Depends(get_current_user)):
    return current_user

@router.delete(
    "/user/{user_id}",
    response_model=Status,
    responses={404: {"model":HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)]
)
async def delete_user(
    user_id: int, current_user: UserOutSchema = Depends(get_current_user)
) -> Status:
    return await crud.delete_user(user_id, current_user)

'''
get_current_user is attached to read_users_me and delete_user in order to protect the routes. Unless the user is logged in as current_user, they won't be able to access them.

/register leverages the crud.create_user helper to create a new user and add it to the database.

/login takes in a user via form data from OAuth2PasswordRequestForm containing the username and password. It then calls the validate_user function with the user or throws an exception if None. An access token is generated from the create_access_token function and then attached to the response header as a cookie.

/users/whoami takes in get_current_user and sends back the results as a response.

/user/{user_id} is a dynamic route that takes in the user_id and sends it to the crud.delete_user helper with the results from current_user.
'''