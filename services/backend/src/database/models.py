from tortoise import fields, models
import datetime

class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __init__(self, username: str, password: str, created_at: datetime.datetime, modified_at: datetime.datetime):
        self.username = username
        self.password = password
        self.created_at = created_at
        self.modified_at = modified_at


class Tasks(models.Model):

    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225)
    comments = fields.TextField(null=True)
    priority_level = fields.IntField(min_value=1, max_value = 5)
    due_date = fields.DatetimeField()
    user = fields.ForeignKeyField("models.Users", related_name="task")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.user_id} on {self.created_at}"
    
    def __init__(self, title:str, comments:str, priority_level:int, due_date:datetime.datetime, user:Users):
        self.title = title
        self.comments = comments
        self.priority_level = priority_level
        self.due_date = due_date
        self.user = user
