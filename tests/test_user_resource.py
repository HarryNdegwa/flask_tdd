import json

from tests.base import BaseCase

class UserResourceTestCase(BaseCase):

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
        self.user3_creation_payload = {
            "username":"CoreyMS",
            "email":"coreyms@gmail.com",
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
        res2 = client.post("/login/",json=login_payload)
        data = json.loads(res2.data)
        self.assertIn("token",data.keys())
        self.assertEqual(res2.status_code,200)
        return data.get("token")


    def token_valid(self,token):
        from app import config
        from resources.user_resource import User
        is_valid = User.validate_token(token,config.get("JWT_SECRET"))
        return is_valid


    def test_list_users(self):
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            token = self.login_user(client)
            token_valid = self.token_valid(token)
            res = client.get("/users/",headers={"Authorization":f"Bearer {token}"})
            data = json.loads(res.data.decode("utf-8"))
            self.assertIsInstance(data,list)


    def test_list_users_with_invalid_token(self):
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDg1Nzk3MDIsImV4cCI6MTYwODU4MDAwMiwic3ViIjoxfQ.Xb8ak1mNwFjzVzr4_4DTVocLi4JN1oIhZLpVOY2VMxE"
            token_valid = self.token_valid(token)
            res = client.get("/users/",headers={"Authorization":f"Bearer {token}"})
            data = json.loads(res.data.decode("utf-8"))
            self.assertIsInstance(data,str)



    def test_user_creation(self):
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)


    def test_user_creation_with_invalid_payload(self):
        with self.app as client:
            res = client.post("/users/",json=self.invalid_user_creation_payload)
            data = json.loads(res.data)
            self.assertIn("message",data.keys())
            self.assertEqual(res.status_code,400)


    def test_user_creation_with_existing_username(self):
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            res2 = client.post("/users/",json=self.username_user_payload)
            data = json.loads(res2.data)
            self.assertEqual(data,"Username already exists!")
            self.assertEqual(res2.status_code,400)


    def test_user_creation_with_existing_email(self):
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            res2 = client.post("/users/",json=self.email_user_payload)
            data = json.loads(res2.data)
            self.assertEqual(data,"Email already exists!")
            self.assertEqual(res2.status_code,400)



    def test_get_user_by_valid_id(self):
        test_id = 1
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            res2 = client.get(f"/user/{test_id}/")
            data = json.loads(res2.data)
            self.assertEqual(data.get("id"),test_id)
            self.assertIn("username",data.keys())
            self.assertEqual(res2.status_code,200)


    def test_get_user_by_invalid_id(self):
        test_id = 100
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            res2 = client.get(f"/user/{test_id}/")
            data = json.loads(res2.data)
            self.assertEqual(data.get("message"),f"User {test_id} does not exist!")
            self.assertEqual(res2.status_code,404)


    def test_update_valid_user(self):
        test_id = 1
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            res2 = client.put(f"/user/{test_id}/",json=self.update_payload)
            self.assertEqual(res2.status_code,204)


    def test_update_invalid_user(self):
        test_id = 100
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            res2 = client.put(f"/user/{test_id}/",json=self.update_payload)
            self.assertEqual(res2.status_code,404)


    def test_delete_valid_user(self):
        test_id = 1
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            res2 = client.delete(f"/user/{test_id}/")
            self.assertEqual(res2.status_code,204)


    def test_delete_invalid_user(self):
        test_id = 100
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload)
            res2 = client.delete(f"/user/{test_id}/")
            self.assertEqual(res2.status_code,404)


    def test_user_login_with_valid_credentials(self):
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload) 
            self.login_user(client)


    def test_user_login_with_invalid_credentials(self):
        with self.app as client:
            self.create_test_user(client,self.user1_creation_payload) 
            login_payload = {
                "email":"harryndegwa@gmail.com",
                "password":"testuser"
            }
            res2 = client.post("/login/",json=login_payload)
            data = json.loads(res2.data)
            self.assertIsInstance(data,str)
            self.assertEqual(data,"Wrong email or password!")
            self.assertEqual(res2.status_code,404)

    
    def create_user_and_follow(self,client):
        # create user doing the following
        self.create_test_user(client,self.user1_creation_payload) # id = 1
        # login this user
        token = self.login_user(client)
        # create another user to be followed
        self.create_test_user(client,self.user2_creation_payload) # id = 2
        # follow this user
        res = client.post("/follow/",json={"id":2},headers={"Authorization":f"Bearer {token}"})
        data = json.loads(res.data)
        user1_following = data[0]
        user2_followed = data[1]
        self.assertIsInstance(user1_following,list)
        self.assertIsInstance(user2_followed,list)
        self.assertIn(2,user1_following)
        self.assertIn(1,user2_followed)
        self.assertEqual(res.status_code,201)


    def test_user_follow(self):
        with self.app as client:
            self.create_user_and_follow(client)






            