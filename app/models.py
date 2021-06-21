from sqlalchemy.orm import backref
from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Quote:
    '''
    Quote class define quote objects
    '''
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    posts = db.relationship('Post', backref='user', lazy = 'dynamic')
    comment = db.relationship('Comment', backref='user', lazy = 'dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
    def __repr__(self):
        return f'User: {self.username}'


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic') 


    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_user_posts(cls,id):
        posts = Post.query.filter_by(user_id = id).order_by(Post.date_posted.desc()).all()
        return posts

    @classmethod
    def get_all_posts(cls):
        return Post.query.order_by(Post.date_posted).all()

    def __repr__(self):
        return f'Post:{self.title}'


@classmethod                            
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(post_id = id).all()
        return comments

    @classmethod
    def delete_comment(cls, id):
        delete_comment = Comment.query.filter_by(id = id).first()
        db.session.delete(delete_comment)
        db.session.commit()

    
    def __repr__(self):
        return f'Post:{self.comment}'
