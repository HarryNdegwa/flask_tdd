import unittest

from flask_sqlalchemy import SQLAlchemy

from app import app,db
from resources.user_resource import User

class BaseCase(unittest.TestCase):

    # test isolation
    def setUp(self):
        self.app = app.test_client()
        self.db = db
        self.user = User
        
    def tearDown(self):
        self.db.drop_all()