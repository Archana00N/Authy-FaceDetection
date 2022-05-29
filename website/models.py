# from enum import unique
from . import db # from website folder import db
from flask_login import UserMixin # flask package to login
from sqlalchemy.sql import func # to get current date and time

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # foriegn key attribute

class User(db.Model, UserMixin): # Usermixin only for User class ## Model inherited from db
    # define all the db schema
    id = db.Column(db.Integer, primary_key=True) # primary key of User = id
    email = db.Column(db.String(150), unique=True) # max len = 150, is unique
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    photos = db.relationship('Photo') # relationship referencing name of class
    