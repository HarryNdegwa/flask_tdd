from datetime import datetime

from flask_restful import Resource,reqparse,fields,marshal_with

from app import db


class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer,primary_key=True)
    owner_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    content = db.Column(db.String,nullable=False)
    comments = db.relationship("Comment",backref="post")
    created_at = db.Column(db.DateTime,default=datetime.utcnow)


    def __init__(self,owner_id,content):
        self.owner_id = owner_id
        self.content = content
    

    def __str__(self):
        return self.content


    def get_owner_id(self):
        return self.owner_id





class PostList(Resource):

    resource_fields = {
        "id":fields.Integer,
        "content":fields.String
    }


    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument("content",type=str,required=True,help="Post content required!")


    @marshal_with(resource_fields)
    def post(self):
        req_data = self.post_parser.parse_args()
        post = Post(1,content=req_data.get("content"))
        db.session.add(post)
        db.session.commit()
        post = Post.query.filter_by(id=1).first()
        return post,201