import unittest

from models import User


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User("Harrison","Ndegwa","Ndech","harryndegwa4@gmail.com")


