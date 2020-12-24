from datetime import datetime

from flask import request
from flask_restful import Resource,reqparse

from app import db,ma,config

def is_authenticated(request):
    auth_header = request.headers.get("Authorization")
    if auth_header:
        from resources.user_resource import User
        _,token = auth_header.split(" ")
        token_payload = User.decode_user_token(token,config.get("JWT_SECRET"))
        try:
            subject = token_payload["sub"]
            user = User.query.filter_by(id=int(subject)).first()
            if user:
                return True,user
            return False,{}
        except Exception as e:
            return False,{}
    else:
        return False,{}


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


class PostSchema(ma.Schema):

    class Meta:
        model = Post
        fields = ["id","owner_id","content","comments","created_at"]


post_schema = PostSchema()
posts_schema = PostSchema(many=True)



class PostList(Resource):

    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument("content",type=str,required=True,help="Post content required!")
        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument("id",type=int,required=True,help="User id required!")

    def get(self):
        args = self.get_parser.parse_args()
        is_auth,user = is_authenticated(request)
        if is_auth:
            id_ = args.get("id")
            posts=None
            if id_ == user.id:
                posts = Post.query.filter(Post.owner_id==user.id)
            else:
                posts = Post.query.filter(Post.owner_id==id_)
            return posts_schema.dump(posts),200
        return "",401


    def post(self):
        is_auth,user = is_authenticated(request)
        if is_auth:
            req_data = self.post_parser.parse_args()
            post = Post(owner_id=user.id,content=req_data.get("content"))
            db.session.add(post)
            db.session.commit()
            return "",201
        return "",401