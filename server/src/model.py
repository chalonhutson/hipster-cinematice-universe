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
    message_content = db.Column(db.String(5000), nullable=False)
    message_datetime = db.Column(db.DateTime, nullable=False)

def connect_to_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()


def create_dummy_data():
    hipster = Admin(username="hipstergw", password="password")
    viewer1 = Viewer(twitch_name="Jack", timezone=1, password="password")
    viewer2 = Viewer(twitch_name="Kim", timezone=2, password="password")
    viewer3 = Viewer(twitch_name="Tony", timezone=3, password="password")
    viewer4 = Viewer(twitch_name="David", timezone=4, password="password")
    viewer5 = Viewer(twitch_name="Nina", timezone=6, password="password")
    viewer6 = Viewer(twitch_name="Chloe", timezone=7, password="password")
    message1 = Chat_message(viewer_id=1, message_content="son of a bitch", message_datetime=datetime.now())
    message2 = Chat_message(viewer_id=1, message_content="goddamit", message_datetime=datetime.now())
    message3 = Chat_message(viewer_id=1, message_content="TELL ME WHERE THE BOMB IS!!!!", message_datetime=datetime.now())
    message4 = Chat_message(viewer_id=2, message_content="DAAAAADDD!!!!", message_datetime=datetime.now())
    message5 = Chat_message(viewer_id=3, message_content="iM DA pReSiDeNt!!!", message_datetime=datetime.now())

    data_list = [hipster, viewer1, viewer2, message1, message2, message3, message4]

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
