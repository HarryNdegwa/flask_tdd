from datetime import datetime

from app import db


class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String,nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)


    def __init__(self,content):
        self.content = content
    

    def __str__(self):
        return self.content