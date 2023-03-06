from pymongo import MongoClient
import bcrypt
import datetime
import humanize


class Posts:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.WebPyTest
        self.users = self.db.users
        self.posts = self.db.posts

    def insert_post(self, data):
        inserted = self.posts.insert_one({"username": data.username, "content": data.content, "date_added": datetime.datetime.now()})
        return True

    def get_all_posts(self, username):
        all_posts = []
        for post in self.posts.find({"username": username}):
            post["timestamp"] = humanize.naturaltime(datetime.datetime.now() - post["date_added"])
            all_posts.append(post)
        return all_posts
