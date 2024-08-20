class Story:
    def __init__(self , title, description):
        self.storyid = None
        self.title = title 
        self.description = description
        self.tasks = []
    
    def update_story(self, title = None, description = None):
        if title:
            self.title = title 
        if description:
            self.description = description
    
    def add_task(self, task):
        self.tasks.append(task)
    



    
