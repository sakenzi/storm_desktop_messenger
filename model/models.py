class AuthRegisterData:
    def __init__(self, username, fullname, password):
        self.username = username
        self.fullname = fullname
        self.password = password


    def to_dict(self):
        return {
            "username": self.username,
            "full_name": self.fullname,
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
    

class SearchUser:
    def __init__(self, id, username, full_name, online, last_visit):
        self.id = id
        self.username = username
        self.full_name = full_name
        self.online = online
        self.last_visit = last_visit

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "full_name": self.full_name,
            "online": self.online,
            "last_visit": self.last_visit
        }