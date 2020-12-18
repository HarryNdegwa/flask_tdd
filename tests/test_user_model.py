from models.user import User
from tests.base import BaseCase


class UserModelTestCase(BaseCase):
    
    def setUp(self):
        super().setUp()
        self.user = User("Ndech","Harrison","Ndegwa","harryndegwa4@gmail.com")

    
    def test_user_instance(self):
        self.assertIsInstance(self.user,User)


    def test_user_str(self):
        self.assertEqual(str(self.user),"Ndech")


    def test_user_get_username(self):
        self.assertEqual(self.user.get_username(),"Ndech")

    
    def test_user_get_email(self):
        self.assertEqual(self.user.get_email(),"harryndegwa4@gmail.com")


    