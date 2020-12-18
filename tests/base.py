import unittest

from flask_sqlalchemy import SQLAlchemy

from main import app,db

class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db
        print(dir(db))

    def tearDown(self):
        # Delete Database collections after the test is complete
        # change this to sql stuff
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)