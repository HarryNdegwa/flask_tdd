import unittest

from main import app

class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = get_db()


    def tearDown(self):
        # Delete Database collections after the test is complete
        # change this to sql stuff
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)