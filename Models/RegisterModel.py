import pymongo
from pymongo import MongoClient
import bcrypt


class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.WebPyTest
        self.users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        id = self.users.insert_one({"username": data.username, "email": data.email, "password": hashed}).inserted_id
        print("uid: ", id)
