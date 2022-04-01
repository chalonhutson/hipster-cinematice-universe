from os import environ

from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config["ENV"] = "development"
app.config["SQLALCHEMY_DATABASE_URI"] = environ["POSTGRES_URI"]
print(app.config["SQLALCHEMY_DATABASE_URI"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


db = SQLAlchemy(app)

Migrate(app, db)

import src.controller as ctrl

@app.route('/hello')
def hello_world():
    return jsonify({"data": "Hello, World!"})

@app.route("/add-admin/", methods=["POST"])
def add_admin():
    print(request.get_data())
    return jsonify({"res": "Cool beans"}), 201
    # res = ctrl.add_admin(
    #     {"username": username,
    #     "password": generate_password_hash(password)}
    #     )

    # if res:
    #     return jsonify({"res": "success"}), 201
    # else:
    #     return jsonify({"res": "failed"}), 404

