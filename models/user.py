from main import db

db = SQLAlchemy(app)

class User(db.Model):
    

    __tablename__ = "users"

    username = db.Column(db.String,nullable=False)
    first_name = db.Column(db.String,nullable=True)
    last_name = db.Column(db.String,nullable=True)
    email = db.Column(db.String,nullable=False)


    def __str__(self):
        return self.username