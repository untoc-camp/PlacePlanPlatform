
class UserModel:
    def __init__(self, json):
        self.user_id = json["user_id"]
        self.user_name = json["user_name"]
        self.user_password = json["user_password"]
        
    def toJson(self):
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "user_password": self.user_password  
        }
    
    def deleteUser(self):
        self.user_id = ""
        self.user_name = ""
        self.user_password = ""

def setUserModel(json):
    global user
    user =UserModel(json)

