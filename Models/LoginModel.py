import pymongo
from pymongo import MongoClient
import bcrypt


class LoginModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.WebPyTest
        self.users = self.db.users

    def check_user(self, data):
        user = self.users.find_one({"username": data.username})
        if user:
            if bcrypt.checkpw(data.password.encode(), user["password"]):
                return user
            else:
                return False
        else:
            return False

    def update_user(self, user, email):

        result = self.users.update_one({'username': user["username"]}, {'$set': {"email": email}})
        updated = self.users.find_one({"username": user["username"]})

        return updated
