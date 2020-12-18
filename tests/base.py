import unittest

from flask_sqlalchemy import SQLAlchemy

from main import app,db

class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db
        # print(dir(db))

    def tearDown(self):
        self.db.drop_all()