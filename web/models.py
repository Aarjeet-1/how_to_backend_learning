#database models

from . import  db   #access from __init__.py

from flask_login import UserMixin

from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    data = db.Column(db.DateTime(timezone=True),default=func.now())
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))


class Remainder():
    pass



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    notees = db.relationship('Note')

