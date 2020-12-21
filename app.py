import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from config import *


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

app_env = os.environ.get("FLASK_ENV")


if app_env == "testing":
    app.config.from_object(TestingConfig())
    print(app.config)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:harry1998@127.0.0.1:5432/test"
elif app_env == "development":
    app.config.from_object(DevelopmentConfig())
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:harry1998@127.0.0.1:5432/flask_tdd"
elif app_env == "production":
    app.config.from_object(ProductionConfig())
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:harry1998@127.0.0.1:5432/flask_tdd"


db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

api = Api(app)

migrate = Migrate(app,db)


def create_resources():

    from resources.user_resource import UserList,UserDetails
    from resources.post_resource import PostList

    api.add_resource(UserList,"/users/")
    api.add_resource(UserDetails,"/user/<int:id>/")
    api.add_resource(PostList,"/posts/")

create_resources()




if __name__ == "__main__":
    app.run()