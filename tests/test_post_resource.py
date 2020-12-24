import json

from tests.base import BaseCase

class PostResourceTestCase(BaseCase):

    def setUp(self):
        super().setUp()
        self.user1_creation_payload = {
            "username":"CodeYouEmpire",
            "email":"harryndegwa4@gmail.com",
            "password":"testuser"
        }
        
        self.user2_creation_payload = {
            "username":"Pixenweb",
            "email":"contact@pixenweb.com",
            "password":"testuser"
        }


    def create_test_user(self,client,payload):
        res = client.post("/users/",json=payload)
        data = json.loads(res.data)
        self.assertEqual(data,"User created successfully!")
        self.assertEqual(res.status_code,201)

    def login_user(self,client):
        login_payload = {
            "email":"harryndegwa4@gmail.com",
            "password":"testuser"
        }
        res = client.post("/login/",json=login_payload)
        data = json.loads(res.data)
        self.assertIn("token",data.keys())
        self.assertEqual(res.status_code,200)
        return data.get("token")

    def create_test_post(self,client,token):
        user_id = 1
        post_data = {
            "owner_id":user_id,
            "content":"Test post"
        }
        res = client.post("/posts/",json=post_data,headers={"Authorization":f"Bearer {token}"})
        data = json.loads(res.data)
        self.assertIsInstance(data,str)
        self.assertEqual(res.status_code,201)


    def test_get_my_posts(self):
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            token = self.login_user(client)
            res = client.get("/posts/",json={"id":1},headers={"Authorization":f"Bearer {token}"})
            data = json.loads(res.data)
            self.assertIsInstance(data,list)
            self.assertEqual(res.status_code,200)


    def test_get_other_user_posts(self):
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload) # id=1
            token = self.login_user(client)
            self.create_test_user(client,self.user2_creation_payload) # id=2
            res = client.get("/posts/",json={"id":2},headers={"Authorization":f"Bearer {token}"})
            data = json.loads(res.data)
            self.assertIsInstance(data,list)
            self.assertEqual(res.status_code,200)

    
    def test_post_creation(self):
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            token = self.login_user(client)
            self.create_test_post(client,token)

    
    def test_get_post(self):
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            token = self.login_user(client)
            self.create_test_post(client,token)
            res = client.get("/post/1/",headers={"Authorization":f"Bearer {token}"})
            data = json.loads(res.data)
            self.assertIn("id",data.keys())
            self.assertEqual(res.status_code,200)

    
    def test_get_invalid_post(self):
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            token = self.login_user(client)
            self.create_test_post(client,token)
            res = client.get("/post/100/",headers={"Authorization":f"Bearer {token}"})
            data = json.loads(res.data)
            self.assertIsInstance(data,dict)
            self.assertIn("message",data.keys())
            self.assertEqual(data.get("message"),"Post 100 not found!")
            self.assertEqual(res.status_code,404)


