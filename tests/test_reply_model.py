from tests.base import BaseCase


class ReplyModelTestCase(BaseCase):

    def setUp(self):
        super().setUp()
        self.reply = self.Reply("Test comment reply")


    def test_reply_str(self):
        self.assertEqual(str(self.reply),"Test comment reply")