import os
from werkzeug.security import generate_password_hash, check_password_hash
from config import db, login_manager, app

@login_manager.user_loader
def load_user(user):
    return User.get(user)


class User(db.Model):
    __tablename__   = 'users'    
    id              = db.Column('user_id', db.Integer, primary_key = True)
    username        = db.Column('username', db.String(50), unique = True, index = True)
    password        = db.Column('password', db.String(255))
    email           = db.Column('email', db.String(50), unique = True, index = True)


    def __init__(self, username, password, email):
        self.username   = username
        self.set_password(password)
        self.email      = email
        
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def chack_password(self, password):
        self.password = check_password_hash
        
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return unicode(self.id)
    
    def __repr__(self) -> str:
        return '<User %r>' % (self.username)