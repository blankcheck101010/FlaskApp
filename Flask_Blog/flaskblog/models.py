from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin
# create a decorated function for login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# We will be using classes as models
# The class below inherits from db.Model
# Each class will be it's own table in the database


class User(db.Model, UserMixin):  # table name defaults to lowercase version of class name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)  # 60 char because hashing algorithm is 60 char output
    posts = db.relationship('Post', backref='author', lazy=True)  # This is not a column!
    # backref - allows is to add a column to the Post model below.
    # When we have a post, we can simply use the 'author' attribute to find out who created the post
    # The lazy argument defines when SQL Alchemy loads data to the database

    # Double underscore methods are also called dunder or magic methods

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # here user.id is our foreign key

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


if __name__ == '__main__':
    app.run(debug=True)
