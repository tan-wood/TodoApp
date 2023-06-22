from src.crud.tasks import TaskCRUD
from src.database.models import Tasks

class TestTasks:
    
    def test_create_task_integration(self):
        # TODO: get this to actually work
        task = Tasks("test")
        TaskCRUD.create_task()