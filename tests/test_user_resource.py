import json

from tests.base import BaseCase

class UserResourceTestCase(BaseCase):

    def setUp(self):
        super().setUp()
        self.user_creation_payload = {
            "username":"CodeYouEmpire",
            "email":"harryndegwa4@gmail.com",
            "password":"testuser"
        }

    def test_list_users(self):
        with self.app as client:
            get_req = client.get("/users/")
            data = json.loads(get_req.data.decode("utf-8"))
            self.assertIsInstance(data,list)


    def test_user_creation(self):
        with self.app as client:
            post_req = client.post("/users/",json=self.user_creation_payload)
            data = json.loads(post_req.data)
            self.assertEqual(data,"User created successfully!")