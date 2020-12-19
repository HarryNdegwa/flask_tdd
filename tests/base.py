import unittest

from flask_sqlalchemy import SQLAlchemy

from app import app,db

class BaseCase(unittest.TestCase):

    # test isolation
    def setUp(self):
        self.app = app.test_client()
        self.db = db
        
    def tearDown(self):
        self.db.drop_all()