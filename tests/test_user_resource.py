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

        self.invalid_user_creation_payload = {
            "email":"harryndegwa4@gmail.com",
            "password":"testuser"
        }

        self.username_user_payload = {
            "username":"CodeYouEmpire",
            "email":"harryndegwa4@gmail.com",
            "password":"testuser"
        }

        self.email_user_payload = {
            "username":"test",
            "email":"harryndegwa4@gmail.com",
            "password":"testuser"
        }

        self.update_payload = {
            "username":"test",
        }

    def test_list_users(self):
        with self.app as client:
            res = client.get("/users/")
            data = json.loads(res.data.decode("utf-8"))
            self.assertIsInstance(data,list)


    def test_user_creation(self):
        with self.app as client:
            res = client.post("/users/",json=self.user_creation_payload)
            data = json.loads(res.data)
            self.assertEqual(data,"User created successfully!")
            self.assertEqual(res.status_code,201)


    def test_user_creation_with_invalid_payload(self):
        with self.app as client:
            res = client.post("/users/",json=self.invalid_user_creation_payload)
            data = json.loads(res.data)
            self.assertIn("message",data.keys())
            self.assertEqual(res.status_code,400)


    def test_user_creation_with_existing_username(self):
        with self.app as client:
            res1 = client.post("/users/",json=self.user_creation_payload)
            data = json.loads(res1.data)
            self.assertEqual(data,"User created successfully!")
            self.assertEqual(res1.status_code,201)
            res2 = client.post("/users/",json=self.username_user_payload)
            data = json.loads(res2.data)
            self.assertEqual(data,"Username already exists!")
            self.assertEqual(res2.status_code,400)


    def test_user_creation_with_existing_email(self):
        with self.app as client:
            res1 = client.post("/users/",json=self.user_creation_payload)
            data = json.loads(res1.data)
            self.assertEqual(data,"User created successfully!")
            self.assertEqual(res1.status_code,201)
            res2 = client.post("/users/",json=self.email_user_payload)
            data = json.loads(res2.data)
            self.assertEqual(data,"Email already exists!")
            self.assertEqual(res2.status_code,400)



    def test_get_user_by_valid_id(self):
        test_id = 1
        with self.app as client:
            res1 = client.post("/users/",json=self.user_creation_payload)
            data = json.loads(res1.data)
            self.assertEqual(data,"User created successfully!")
            self.assertEqual(res1.status_code,201)
            res2 = client.get(f"/user/{test_id}/")
            data = json.loads(res2.data)
            self.assertEqual(data.get("id"),test_id)
            self.assertIn("username",data.keys())
            self.assertEqual(res2.status_code,200)


    def test_get_user_by_invalid_id(self):
        test_id = 100
        with self.app as client:
            res1 = client.post("/users/",json=self.user_creation_payload)
            data = json.loads(res1.data)
            self.assertEqual(data,"User created successfully!")
            self.assertEqual(res1.status_code,201)
            res2 = client.get(f"/user/{test_id}/")
            data = json.loads(res2.data)
            self.assertEqual(data.get("message"),f"User {test_id} does not exist!")
            self.assertEqual(res2.status_code,404)


    def test_update_valid_user(self):
        test_id = 1
        with self.app as client:
            res1 = client.post("/users/",json=self.user_creation_payload)
            data = json.loads(res1.data)
            self.assertEqual(data,"User created successfully!")
            self.assertEqual(res1.status_code,201)
            res2 = client.put(f"/user/{test_id}/",json=self.update_payload)
            self.assertEqual(res2.status_code,204)


    def test_update_invalid_user(self):
        test_id = 100
        with self.app as client:
            res1 = client.post("/users/",json=self.user_creation_payload)
            data = json.loads(res1.data)
            self.assertEqual(data,"User created successfully!")
            self.assertEqual(res1.status_code,201)
            res2 = client.put(f"/user/{test_id}/",json=self.update_payload)
            self.assertEqual(res2.status_code,404)
            