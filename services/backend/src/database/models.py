from tortoise import fields, models
import datetime

class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now_add=True)


class Tasks(models.Model):

    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=300)
    comments = fields.TextField(null=True)
    priority_level = fields.IntField(min_value=1, max_value = 5)
    due_date = fields.DatetimeField()
    user = fields.ForeignKeyField("models.Users", related_name="task")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.user_id} on {self.created_at}"
