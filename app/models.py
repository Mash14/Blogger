from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String)
    profile_pic = db.Column(db.String)
    blogs = db.relationship('Blog',backref = 'user',lazy = 'dynamic')
    comments = db.relationship('Comment',backref = 'user',lazy = 'dynamic')
    upvotes = db.relationship('Upvote',backref = 'user',lazy = 'dynamic')
    downvotes = db.relationship('Downvote',backref = 'user',lazy = 'dynamic')

    def __repr__(self):
        return f'User {self.username}'

    # @property to create a write only class property password
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    # generating_password_hash - This function takes in a password and generates a password hash.
    # check_password_hash - This function takes in a hash password and a password entered by a user and checks if the password matches to return a True or False response.
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    post = db.Column(db.String)
    post_time = db.Column(db.DateTime,default = datetime.utcnow)
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'blog',lazy = 'dynamic')
    upvotes = db.relationship('Upvote',backref = 'blog',lazy = 'dynamic')
    downvotes = db.relationship('Downvote',backref = 'blog',lazy = 'dynamic')

    def __repr__(self):
        return f'{self.title}'

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    time = db.Column(db.DateTime,default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))

    def __repr__(self):
        return f'{self.comment}'

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()

class Upvote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))

    def __repr__(self):
        return f'{self.user_id}:{self.blog_id}'

    def save_upvote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvote.query.filter_by(blog_id = id).all()
        return upvote

class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))

    def __repr__(self):
        return f'{self.user_id}:{self.blog_id}'

    def save_downote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(blog_id = id).all()
        return downvote

# for quotes api 
class Quotes():
    def __init__(self,id,author,quote):
        
        self.id = id 
        self.author = author 
        self.quote = quote 