from datetime import datetime

from flask_restful import Resource,reqparse

from app import db,bcrypt


class User(db.Model):
    
    __tablename__ = "users"


    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,nullable=False)
    first_name = db.Column(db.String,nullable=True)
    last_name = db.Column(db.String,nullable=True)
    email = db.Column(db.String,nullable=False)
    created_at = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.utcnow,onupdate=datetime.utcnow)
    password = db.Column(db.String,nullable=False)


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

    def get(self):
        users = User.query.all()
        return users,200

    def post(self):
        data = self.post_req_parser.parse_args()
        if self.username_exists(data.get("username")):
            return "Username already exists!",400
        user = User(username=data.get("username"),first_name=data.get("first_name"),last_name=data.get("last_name"),email=data.get("email"),password=data.get("password"))
        db.session.add(user)
        db.session.commit()
        return "User created successfully!",201

