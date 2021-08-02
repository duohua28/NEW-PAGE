from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "HELLO"

    @app.route('/')
    def home():
        return "<h1>HELLO</h1>"

    @app.route('/profile')
    def profile():
        return "<h1>PROFILE</h1>"

    return app
