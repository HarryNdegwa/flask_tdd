from datetime import datetime

from app import db

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer,primary_key=True)
    post_id = db.Column(db.Integer,db.ForeignKey("posts.id"))
    owner_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)


    def __init__(self,content):
        self.content = content

    def __str__(self):
        return self.content