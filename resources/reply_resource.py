from datetime import datetime

from app import db

class Reply(db.Model):

    __tablename__ = "replies"

    id = db.Column(db.Integer,primary_key=True)
    comment_id = db.Column(db.Integer,db.ForeignKey("comments.id"))
    owner_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)


    def __init__(self,content):
        self.content = content


    def __str__(self):
        return self.content