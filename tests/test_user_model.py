from models import User
from .base import BaseCase


class UserTestCase(BaseCase):
    
    def setUp(self):
        super().setUp()
        self.user = User("Harrison","Ndegwa","Ndech","harryndegwa4@gmail.com")


    def test_user_str(self):
        self.assertEqual(str(self.user),"Ndech")


    