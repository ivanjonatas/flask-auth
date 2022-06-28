from crypt import methods
from distutils.log import debug
import os
from flask import Flask, request, url_for, redirect, render_template
from models.User import User
from config import app, login_manager, db 


@app.route('/')
def home():
    return 'hello from session'

@app.route('/users/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    user = User(request.form['username'], request.form['password'],request.form['email'])
    
    db.session.add(user)
    db.session.commit()
    
    return redirect(url_for('login')) 


@app.route('/login', methods = ['GET'])
def login():
    return 'login'

if __name__ == '__main__':
    app.run(debug = True, port = 5001)