from database import db
from init import app

with app.app_context():
    class User(db.Model):
        __tablename__='user'
        id=db.Column(db.Integer, primary_key=True,autoincrement=True)
        username=db.Column(db.String(16),nullable=False,unique=True)
        password=db.Column(db.String(16),nullable=False)
        email=db.Column(db.String(16),nullable=False)


"""    def find_user_by_name(self, username):
        row = User.query.filter(User.username == username).first()
        return row"""
