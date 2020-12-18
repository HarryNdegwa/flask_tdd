from flask_restful import Resource,reqparse

from main import db

class UserList(Resource):

    def __init__(self):
        self.post_req_parser = reqparse.RequestParser(bundle_errors=True)
        self.post_req_parser.add_argument("username",type=str,required=True,help="Username required!")
        self.post_req_parser.add_argument("first_name",type=str,required=False)
        self.post_req_parser.add_argument("last_name",type=str,required=False)
        self.post_req_parser.add_argument("email",type=str,required=True,help="Email required!")
        self.post_req_parser.add_argument("password",type=str,required=True,help="Password required!")

    def get(self):
        return "",200

    def post(self):
        pass

