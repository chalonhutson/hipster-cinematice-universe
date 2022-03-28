from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User id: {self.id}, username: {self.username}>"

def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from __init__ import app
    connect_to_db(app)
    print("Connected to DB.")
