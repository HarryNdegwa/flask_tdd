import jwt
from datetime import datetime
from functools import wraps

from flask_restful import Resource,reqparse,abort,request
from sqlalchemy.types import ARRAY

from app import db,bcrypt,config,ma
from resources.post_resource import Post
from resources.comment_resource import Comment
from resources.reply_resource import Reply



class User(db.Model):
    
    __tablename__ = "users"


    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,nullable=False)
    first_name = db.Column(db.String,nullable=True)
    last_name = db.Column(db.String,nullable=True)
    email = db.Column(db.String,nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
    password = db.Column(db.String,nullable=False)
    posts = db.relationship("Post",backref="user")
    comments = db.relationship("Comment",backref="owner")
    replies = db.relationship("Reply",backref="owner")
    followers = db.Column(ARRAY(db.Integer),nullable=True)
    following = db.Column(ARRAY(db.Integer),nullable=True)


    def __init__(self,username,first_name,last_name,email,password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")



    def __str__(self):
        return self.username


    def get_username(self):
        return self.username


    def get_email(self):
        return self.email

    
    def get_followers(self):
        return self.followers


    def get_following(self):
        return self.following


    def get_fields(self):
        return ["username","first_name","last_name","email","password"]


    def encode_user_token(self,id,expires,secret):
        import datetime
        try:
            payload = {
                "iat":datetime.datetime.utcnow(),
                "exp":datetime.datetime.utcnow()+datetime.timedelta(days=0,seconds=expires),
                "sub":int(id)
            }
            return jwt.encode(payload,secret,algorithm="HS256")
        except Exception as e:
            print(e)


    @staticmethod
    def decode_user_token(token,secret):
        try:
            payload = jwt.decode(token,secret,algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return "Token expired. Please login again!"
        except  jwt.InvalidSignatureError:
            return "Invalid token. Please login again!" 


    @staticmethod
    def validate_token(token,secret):
        try:
            payload = jwt.decode(token,secret,algorithms=["HS256"])
            return True
        except Exception as e:
            return False



class UserSchema(ma.Schema):

    class Meta:
        model = User
        fields = ["id","username","email"]

user_schema = UserSchema()
users_schema = UserSchema(many=True)



def is_authenticated(request):
    auth_header = request.headers.get("Authorization")
    if auth_header:
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



class UserList(Resource):


    def __init__(self):
        self.post_req_parser = reqparse.RequestParser(bundle_errors=True)
        self.post_req_parser.add_argument("username",type=str,required=True,help="Username required!")
        self.post_req_parser.add_argument("first_name",type=str,required=False)
        self.post_req_parser.add_argument("last_name",type=str,required=False)
        self.post_req_parser.add_argument("email",type=str,required=True,help="Email required!")
        self.post_req_parser.add_argument("password",type=str,required=True,help="Password required!")

    def username_exists(self,name):
        user = User.query.filter_by(username=name).first()
        return user

    def email_exists(self,email):
        user = User.query.filter_by(email=email).first()
        return user

    def get(self):
        if is_authenticated(request):
            users = User.query.all()
            return users_schema.dump(users),200
        return "",401

    def post(self):
        data = self.post_req_parser.parse_args()
        if self.username_exists(data.get("username")):
            return "Username already exists!",400

        if self.email_exists(data.get("email")):
            return "Email already exists!",400

        user = User(username=data.get("username"),first_name=data.get("first_name"),last_name=data.get("last_name"),email=data.get("email"),password=data.get("password"))
        db.session.add(user)
        db.session.commit()
        return "User created successfully!",201


class UserDetails(Resource):


    def __init__(self):
        self.put_parser = reqparse.RequestParser()
        self.put_parser = reqparse.RequestParser(bundle_errors=True)
        self.put_parser.add_argument("username",type=str,required=False)
        self.put_parser.add_argument("first_name",type=str,required=False)
        self.put_parser.add_argument("last_name",type=str,required=False)
        self.put_parser.add_argument("email",type=str,required=False)
        self.put_parser.add_argument("password",type=str,required=False)


    def abort_if_user_does_not_exist(self,id):
        user = self.get_user(id)
        if not user.first():
            return abort(404,message = f"User {id} does not exist!")
        return user


    def get_user(self,id):
        user = User.query.filter_by(id=id)
        if user:
            return user
        return False


    def get(self,id):
        user = self.abort_if_user_does_not_exist(id)
        return user_schema.dump(user.first()),200


    def update_data(self,user,raw_data):
        data = {}
        user_fields = user.first().get_fields()
        for field in user_fields:
            if field in raw_data.keys():
                if raw_data.get(field) == None:
                    data[field] = user.first().__dict__.get(field)
                else:
                    data[field] = raw_data.get(field)
            else:
                data[field] = user.first().__dict__.get(field)
        
        return data


    def put(self,id):
        user = self.abort_if_user_does_not_exist(id)
        request_data = self.put_parser.parse_args()    
        data = self.update_data(user,request_data)
        user.update(data)
        db.session.commit()
        return {},204


    def delete(self,id):
        user = self.abort_if_user_does_not_exist(id)
        db.session.delete(user.first())
        db.session.commit()
        return {},204



class UserLogin(Resource):

    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument("email",type=str,required=True,help="Email is required!")
        self.post_parser.add_argument("password",type=str,required=True,help="Password is required!")

    def post(self):
        req_data = self.post_parser.parse_args()
        user = User.query.filter_by(email = req_data.get("email")).first()
        if not user:
            return "Wrong email or password!",404

        try:
            token = user.encode_user_token(user.id,config.get("TOKEN_EXPIRES"),config.get("JWT_SECRET"))
            return {"token":token.decode()},200
        except Exception as e:
            return "",404




