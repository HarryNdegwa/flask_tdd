from tests.base import BaseCase

class UserResourceTestCase(BaseCase):

    def setUp(self):
        super().setUp()
        self.user_creation_payload = {
            "username":"CodeYouEmpire",
            "email":"harryndegwa4@gmail.com",
            "password":"testuser"
        }


    def test_user_creation(self):
        pass