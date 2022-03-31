from os import environ

from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'

db = SQLAlchemy(app)

Migrate(app, db)

import src.controller as ctrl

@app.route('/hello')
def hello_world():
    return jsonify({"data": "Hello, World!"})

@app.route("/add-admin/<string:username>")
def add_admin(username):
    res = ctrl.add_admin(
        {"username": username,
        "password": "pass"}
        )

    if res:
        return jsonify({"res": "success"}), 201
    else:
        return jsonify({"res": "failed"}), 404

