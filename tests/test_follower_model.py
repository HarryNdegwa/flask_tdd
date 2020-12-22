from tests.base import BaseCase


class FollowerModelTestCase(BaseCase):

    def setUp(self):
        super().setUp()
        self.follower = self.Follower(1,2)


    def test_model_str(self):
        self.assertEqual(str(self.follower),"2 follows 1")
