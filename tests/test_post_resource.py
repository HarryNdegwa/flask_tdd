import json

from tests.base import BaseCase

class PostResourceTestCase(BaseCase):

    def setUp(self):
        super().setUp()
        self.user_creation_payload = {
            "username":"CodeYouEmpire",
            "email":"harryndegwa4@gmail.com",
            "password":"testuser"
        }

    def test_get_user_posts(self):
        with self.app as client:
            res = client.get("/posts/")
            data = json.loads(res.data)
            self.assertIsInstance(data,list)
            self.assertEqual(res.status_code,200)

        

    def test_post_creation(self):
        with self.app as client:
            res1 = client.post("/users/",json=self.user_creation_payload)
            data = json.loads(res1.data)
            self.assertEqual(data,"User created successfully!")
            self.assertEqual(res1.status_code,201)
            user_id = 1
            post_data = {
                "owner_id":user_id,
                "content":"Test post"
            }
            res2 = client.post("/posts/",json=post_data)
            data = json.loads(res2.data)
            self.assertIsInstance(data,str)
            self.assertEqual(res2.status_code,201)

