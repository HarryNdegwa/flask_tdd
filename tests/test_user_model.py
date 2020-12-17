import unittest

from models import User


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User("Harrison","Ndegwa","Ndech","harryndegwa4@gmail.com")


    def test_user_str(self):
        self.assertEqual(str(self.user),"Ndech")


    