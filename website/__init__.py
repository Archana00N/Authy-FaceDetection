from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path  # operating system provides the directory
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "faceLogin.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Microsoft engage project'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)  # initialise database

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from . import models
    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # where the user will be redirected if they're not logged in yet
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # filter by, ckecks fro primary key id

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):  # if doesn't already exist, create
        db.create_all(app=app)
        print('Created Database!')
