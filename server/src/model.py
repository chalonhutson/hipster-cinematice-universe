from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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
    message_content(db.String, nullable=False)
    message_datetime(db.Datetime, nullable=False)

def connect_to_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()


if __name__ == "__main__":
    from __init__ import app
    connect_to_db(app)
    print("Connected to DB.")
