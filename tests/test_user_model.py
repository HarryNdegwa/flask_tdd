from tests.base import BaseCase


class UserModelTestCase(BaseCase):
    
    def setUp(self):
        super().setUp()
        self.user = self.User("Ndech","Harrison","Ndegwa","harryndegwa4@gmail.com","testuser")

    
    def test_user_instance(self):
        self.assertIsInstance(self.user,self.User)


    def test_user_str(self):
        self.assertEqual(str(self.user),"Ndech")


    def test_user_get_username(self):
        self.assertEqual(self.user.get_username(),"Ndech")

    
    def test_user_get_email(self):
        self.assertEqual(self.user.get_email(),"harryndegwa4@gmail.com")


    def test_encode_user_token(self):
        user_id = 1
        token = self.encode_user_token(user_id).decode()
        token_sections = token.split(".")
        self.assertEqual(len(token_sections),3)
        



        


    