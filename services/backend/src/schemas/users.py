from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Users

UserInSchema = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True
)
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)

#Schemas:

# UserInSchema is for creating new users.
# UserOutSchema is for retrieving user info to be used outside our application, for returning to end users.
# UserDatabaseSchema is for retrieving user info to be used within our application, for validating users.