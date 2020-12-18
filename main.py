import os

from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

testing = os.environ.get("TESTING")

database = None

if testing:
    app.testing = True
    database = app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:harry1998@127.0.0.1:5432/test"
else:
    database = app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:harry1998@127.0.0.1:5432/flask_tdd"


if __name__ == "__main__":
    app.run(debug=True)