import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

testing = os.environ.get("TESTING")

if testing:
    app.testing = True
    db_config = app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:harry1998@127.0.0.1:5432/test"
else:
    db_config = app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:harry1998@127.0.0.1:5432/flask_tdd"

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

if __name__ == "__main__":
    app.run(debug=True)