from tests.base import BaseCase

class PostModelTestCase(BaseCase):

    def setUp(self):
        super().setUp()
        self.post = self.Post()

    def test_post_str(self):
        self.assertEqual(str(self.post),"Test post")