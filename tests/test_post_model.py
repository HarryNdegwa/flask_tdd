from tests.base import BaseCase

class PostModelTestCase(BaseCase):

    def setUp(self):
        super().setUp()
        self.post = self.Post(1,"Test post")

    def test_post_str(self):
        self.assertEqual(str(self.post),"Test post")


    def test_type_post_owner_id(self):
        self.assertIsInstance(self.post.get_owner_id(),int)