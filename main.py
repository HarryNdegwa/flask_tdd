import os

from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

testing = os.environ.get("TESTING")

database = None

if testing:
    print("Testing")
    # database = app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:harry1998@127.0.0.1:5432/test_db"
else:
    print("Serious stuff")
    # database = app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:harry1998@127.0.0.1:5432/prod_db"


if __name__ == "__main__":
    app.run(debug=True)