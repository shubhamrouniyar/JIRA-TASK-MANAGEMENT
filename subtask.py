from task import Task

class Subtask(Task):
    def __init__(self, title, description, deadline, assigned_user, status, datetime, parent_id ):
        super().__init__(title, description, deadline, assigned_user, status, datetime)
        self.parent_id = parent_id
    