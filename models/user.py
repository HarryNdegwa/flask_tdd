from main import db

class User(db.Model):
    

    __tablename__ = "users"


    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,nullable=False)
    first_name = db.Column(db.String,nullable=True)
    last_name = db.Column(db.String,nullable=True)
    email = db.Column(db.String,nullable=False)


    def __str__(self):
        return self.username