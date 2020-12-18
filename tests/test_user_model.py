from models.user import User
from tests.base import BaseCase


class UserTestCase(BaseCase):
    
    def setUp(self):
        super().setUp()
        self.user = User("Ndech","Harrison","Ndegwa","harryndegwa4@gmail.com")


    def test_user_str(self):
        self.assertEqual(str(self.user),"Ndech")


    