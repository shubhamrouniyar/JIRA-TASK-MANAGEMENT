from user import User
from task import Task
from subtask import Subtask
from story import Story

class Taskmanager:
    def __init__(self):
        self.users =   {}
        self.tasks =   {}
        self.stories = {}
        self.id = 1000
        self.story_id = 2000

    def register_user(self,username , password , email):
        user_obj = User(username, password, email)
        self.users[username] = user_obj
        return user_obj
    
    def login_user(self, username, password):
        user_obj = self.users[username]
        if username in self.users.keys() and self.users[username].verify_password(password):
            print("Logged in sucessfully !!.........")
            return user_obj 
        raise ValueError("Invalid username or password.")
    
    
    def createtask(self, title, description, deadline, assigned_user, status, datetime):
        task_obj = Task(title, description, deadline, assigned_user, status, datetime)
        task_obj.taskid = self.id
        self.tasks[self.id] = task_obj
        self.users[assigned_user].tasks.append(task_obj)
        self.id += 1
        print("A New task has been created with id", task_obj.taskid, "under name", assigned_user)
        return task_obj


    def updatetask(self, taskid,  description = None , deadline = None, status = None):
        if taskid not in self.tasks:
            raise ValueError("task not found......")
        task_obj =  self.tasks[taskid]
        task_obj.update_task(description, deadline, status)

        print("TASK UPDATED SUCCESSFULLYYY>.....")
        return task_obj
        

    def viewtask(self, username):
        if username not in self.users:
            raise ValueError("user not exists..........")
        print("____________________________________")
        print("TOTAL NO OF TASKS CREATED", len(self.tasks))
        print("____________________________________")

        for task in self.users[username].gettask():
            print("Task ID ", task.taskid)
            print("TTILE ", task.description)
            print("STATUS", task.status)
            print("DEADLINE", task.deadline)
            print("____________________________________")


    def deletetask(self, task_id):
        if task_id not in self.tasks.keys():
            raise ValueError("Task not found , please check the task id......")
        task_obj = self.tasks[task_id]
        self.users[task_obj.assigned_user].tasks.remove(task_obj)
        #task_obj.assigned_user.tasks.remove(task_obj)
        del self.tasks[task_id]
        print("successfully deleted the task !!.....")
        return task_obj
    

    # def movetask(self, new_parent_id, task_id):
    #     if task_id not in self.tasks.keys():
    #         raise ValueError("Task not found , please check the task id......")

    #     task = self.tasks[task_id]
    #     new_parent_task = self.tasks[new_parent_id]

    #     self.users[task.assigned_user].tasks.remove(task)
    #     new_parent_task.add_subtask(task)

    #     print("Task move from parent id",task.parent_id, "too..." )
    #     task.parent_id = new_parent_id
    #     print(task.parent_id)


    def createsubtask(self, parentid ,title, description, deadline, assigned_user, status, datetime):
        if parentid not in self.tasks.keys():
            raise ValueError("Task not found , please check the task id......")
        parenttask = self.tasks[parentid]
        subtask = Subtask(title, description, deadline, assigned_user, status, datetime, parentid)
        subtask.taskid = self.id
        self.tasks[subtask.taskid]  = subtask
        self.id += 1
        parenttask.add_subtask(subtask)
        self.users[assigned_user].tasks.append(subtask)
        print(" A SUB TASK IS CREATE SUCCESSFULLY WITH ID",subtask.taskid , "under parent task id", parentid)
        return subtask



    def createstory(self, title, description, task_ids):

        story_obj  = Story(title, description)
        story_obj.storyid = self.story_id
        
        self.stories[story_obj.storyid] = story_obj
        for each_task_id in task_ids:
            story_obj.add_task(self.tasks[each_task_id])
            print("task added successfully to the story")

        self.story_id += 1
        return story_obj




        

