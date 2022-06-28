import os
from flask              import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy   import SQLAlchemy
from flask_login        import LoginManager
from flask_login        import login_user, logout_user, current_user, login_required

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] =  '123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'auth.db')
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
