import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from config import *


app = Flask(__name__)

app_env = os.environ.get("FLASK_ENV")


if app_env == "testing":
    app.config.from_object(TestingConfig())
    
elif app_env == "development":
    app.config.from_object(DevelopmentConfig())

elif app_env == "production":
    app.config.from_object(ProductionConfig())

config = app.config

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

api = Api(app)

migrate = Migrate(app,db)


def create_endpoints():

    from resources.user_resource import UserList,UserDetails
    from resources.post_resource import PostList

    api.add_resource(UserList,"/users/")
    api.add_resource(UserDetails,"/user/<int:id>/")
    api.add_resource(PostList,"/posts/")

create_endpoints()




if __name__ == "__main__":
    app.run()