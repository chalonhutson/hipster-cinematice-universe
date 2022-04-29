from os import environ

from flask import Flask, jsonify, request, json
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config["ENV"] = "development"
app.config["SQLALCHEMY_DATABASE_URI"] = environ["POSTGRES_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


db = SQLAlchemy(app)

Migrate(app, db)

import src.controller as ctrl

@app.route('/hello')
def hello_world():
    return jsonify({"data": "Hello, World!"})

@app.route("/check-admin", methods=["POST"])
def check_admin():
    check = ctrl.check_admin(request.form)
    if check:
        return "success"
    else:
        return "fail"

@app.route("/add-admin/", methods=["POST"])
def add_admin():
    print(request.get_data())
    return jsonify({"res": "Cool beans"})

    res = ctrl.add_admin(
        {
        "username": req["username"],
        "password": generate_password_hash(req["password"])
        }
    )

    if res:
        return jsonify({"res": "success"}), 201
    else:
        return jsonify({"res": "failed"}), 404
        

@app.route("/login", methods=["POST"])
def login():
    req = request.get_data()

    if req["is_admin"] == True:
        pass


@app.route("/get-messages/<viewer_id>")
def get_messages(viewer_id):
    print(viewer_id)
    return jsonify(ctrl.get_viewer_messages(viewer_id))

@app.route("/get-redemptions/<viewer_id>")
def get_redemptions(viewer_id):
    return jsonify(ctrl.get_viewer_redemptions(viewer_id))


@app.route("/get-viewer-id/<name>")
def get_viewer_id(name):
    return jsonify(ctrl.get_viewer_id(name))    
