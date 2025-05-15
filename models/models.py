class AuthRegisterData:
    def __init__(self, username, fullname, password):
        self.username = username
        self.fullname = fullname
        self.password = password


    def to_dict(self):
        return {
            "username": self.username,
            "fullname": self.fullname,
            "password": self.password
        }
    

class AuthLoginData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password
        }