from main import db,bcrypt

class User(db.Model):
    

    __tablename__ = "users"


    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,nullable=False)
    first_name = db.Column(db.String,nullable=True)
    last_name = db.Column(db.String,nullable=True)
    email = db.Column(db.String,nullable=False)
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