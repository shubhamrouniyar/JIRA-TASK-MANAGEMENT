class Task:
    def __init__(self, title, description, deadline, assigned_user, status, datetime):
        self.taskid = None
        self.title = title
        self.description = description
        self.deadline = deadline 
        self.assigned_user = assigned_user
        self.status = 'NOT_STARTED'
        self.datetime = datetime
        self.sub_tasks = []
    
    def add_subtask(self, subtask):
        self.sub_tasks.append(subtask)
    
    def update_task(self, description = None , deadline = None, status = None):
        if description:
            self.description = description
        if deadline:
            self.deadline = deadline
        if status:
            self.status = status

    

