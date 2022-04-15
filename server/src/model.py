from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import environ
from datetime import datetime

if __name__ == "src.model":
    from src import db

db = SQLAlchemy()


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return f"<User id: {self.id}, username: {self.username}>"

class Viewer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    twitch_name = db.Column(db.String(80), unique=True, nullable=False)
    timezone = db.Column(db.Integer, nullable=True)
    password = db.Column(db.String(120), unique=False, nullable=False)
    messages = db.relationship("Chat_message", backref='viewer', lazy=True)


class Chat_message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    viewer_id = db.Column(db.Integer, db.ForeignKey("viewer.id"), nullable=False)
    content = db.Column(db.String(5000), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    hipster_points = db.Column(db.Integer, default=1, nullable=False)
    fulfilled = db.Column(db.Boolean, nullable=False, default=True)
    hipster_notes = db.Column(db.String(5000), nullable=True)

class Redemption(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    viewer_id = db.Column(db.Integer, db.ForeignKey("viewer.id"), nullable=False)
    redemption = db.Column(db.String(5000), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    hipster_points = db.Column(db.Integer, default=1, nullable=False)
    fulfilled = db.Column(db.Boolean, nullable=False, default=True)
    hipster_notes = db.Column(db.String(5000), nullable=True)


def connect_to_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()


def create_dummy_data():

    data_list = [
        Admin(username="hipstergw", password="password"),
        Viewer(twitch_name="Jack", timezone=1, password="password"),
        Viewer(twitch_name="Kim", timezone=2, password="password"),
        Viewer(twitch_name="Tony", timezone=3, password="password"),
        Viewer(twitch_name="David", timezone=4, password="password"),
        Viewer(twitch_name="Nina", timezone=6, password="password"),
        Viewer(twitch_name="Chloe", timezone=7, password="password"),
        Chat_message(viewer_id=1, content="goddamit", datetime=datetime.now()),
        Chat_message(viewer_id=1, content="GIVE ME MY DAUGHTER!!!!", datetime=datetime.now()),
        Chat_message(viewer_id=1, content="TELL ME WHERE THE BOMB IS!!!!", datetime=datetime.now()),
        Chat_message(viewer_id=2, content="DAAAAADDD!!!!", datetime=datetime.now()),
        Chat_message(viewer_id=3, content="iM DA pReSiDeNt!!!", datetime=datetime.now()),
        Redemption(viewer_id=1, redemption="Shout out!", hipster_points=1, datetime=datetime.now()),
    ]

    for data in data_list:
        db.session.add(data)
        db.session.commit()
    
    

def delete_all_data():
    admins = Admin.query.all()
    viewers = Viewer.query.all()
    messages = Chat_message.query.all()

    delete_list = admins + viewers + messages

    for i in delete_list:
        db.session.delete(i)

    db.session.commit()


if __name__ == "__main__":
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = environ["POSTGRES_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    # from __init__ import app
    connect_to_db(app)
    print("Connected to DB.")
    print(f"Admins = {Admin.query.count()}")
    print(f"Viewers = {Viewer.query.count()}")
    print(f"Messages = {Chat_message.query.count()}")
    print(f"Redemptions = {Redemption.query.count()}")
