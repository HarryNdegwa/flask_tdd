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
        with self.app as client:
            post_req = client.post("/user/create",self.user_creation_payload)
            self.assertEqual(post_req,"User created successfully!")