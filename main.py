from taskmanager import Taskmanager


if __name__ == "__main__":
    
    task_manager = Taskmanager()

    # Register Users 
    task_manager.register_user('kushubham', 'Helloworld', 'shubham@gmail.com')
    task_manager.register_user('kanu', 'Test123', 'kanurastogi@gmail.com')

    # Take sample input for User login 
    username = "kushubham"
    password = "Helloworld"

    curr_user = task_manager.login_user(username , password)

     #create a JIRA TASK 
    task_obj =  task_manager.createtask("design classes of taskmanager" , "create relevant apsi", "28-Aug-2020", "kushubham", "CREATED", "20-Aug-2020")
    #task_obj2 =  task_manager.createtask("test move func class " , "test move func class", "28-Aug-2020", "kushubham", "CREATED", "20-Aug-2020")

    # create a sub task
    subtask_obj = task_manager.createsubtask(task_obj.taskid, "implement inheritence" , "create subclass ", "28-Aug-2020", "kushubham", "CREATED", "20-Aug-2020")

    #create a JIRA STORY 
    task_manager.createstory("taskmanager"," design the taskmanager app from scratch", [task_obj.taskid])

    #VIEW ALL TASKS ASSIGNED TO USER1
    task_manager.viewtask(curr_user.username)

    # Update the task ......
    update_task = task_manager.updatetask(task_obj.taskid, "create apis like createtask() , updatetask(), viewtask() , delete() etc...", "09-Nov-2020", "PENDING")

    # After update lets view the task 
    task_manager.viewtask(curr_user.username)

    #Delete the task
    delete_task = task_manager.deletetask(subtask_obj.taskid)


    task_manager.viewtask(curr_user.username)

    #move the task
    # new_parent_id = 1001
    # task_manager.movetask(new_parent_id, subtask_obj.taskid)










    
