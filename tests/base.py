import unittest

from flask_sqlalchemy import SQLAlchemy

from app import app,db
from resources.user_resource import User
from resources.post_resource import Post
from resources.comment_resource import Comment
from resources.reply_resource import Reply

class BaseCase(unittest.TestCase):
        

    # test isolation
    def setUp(self):
        self.app = app.test_client()
        self.db = db
        self.db.create_all()
        self.User = User
        self.Post = Post
        self.Comment = Comment
        self.Reply = Reply
        self.jwt_secret = app.config["JWT_SECRET"]

        
    def tearDown(self):
        self.db.drop_all()