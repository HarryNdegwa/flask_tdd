import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

testing = os.environ.get("TESTING")

if testing:
    app.testing = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:harry1998@127.0.0.1:5432/test"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:harry1998@127.0.0.1:5432/flask_tdd"

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

api = Api(app)

migrate = Migrate(app,db)


def create_resources():

    from resources.user_resource import UserList

    api.add_resource(UserList,"/users/")

create_resources()




if __name__ == "__main__":
    app.run(debug=True)