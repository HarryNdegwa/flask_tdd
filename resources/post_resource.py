from datetime import datetime

from flask_restful import Resource,reqparse

from app import db,ma


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
        self.post_parser.add_argument("owner_id",type=int)
        self.post_parser.add_argument("content",type=str,required=True,help="Post content required!")

    def get(self):
        return posts_schema.dump(Post.query.all()),200


    def post(self):
        req_data = self.post_parser.parse_args()
        post = Post(owner_id=req_data.get("owner_id"),content=req_data.get("content"))
        db.session.add(post)
        db.session.commit()
        return "",201