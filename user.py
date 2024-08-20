class User:
    def __init__(self, username , password, email):
        self.username =  username
        self.password = password 
        self.email = email
        self.tasks = []

    def verify_password(self, password):
        if self.password == password:
            return True
        return False
    
    def gettask(self):
        return self.tasks
