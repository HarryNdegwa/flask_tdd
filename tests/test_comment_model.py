from tests.base import BaseCase

class CommentModelTestCase(BaseCase):

    def setUp(self):
        super().setUp()
        self.comment = self.Comment("First post comment")


    def test_comment_str(self):
        self.assertEqual(str(self.comment),"First post comment")