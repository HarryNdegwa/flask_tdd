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
        self.jwt_secret = "\xd1\xd7\xee_\xab\xd0UB:\x18\x1bh8\xc8\x90\x0eb+\xc67R\xec^\x90"
        
    def tearDown(self):
        self.db.drop_all()