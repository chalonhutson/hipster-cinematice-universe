from flask import Flask, jsonify
import src.controller as ctrl

app = Flask(__name__)



@app.route('/hello')
def hello_world():
    return jsonify({"data": "Hello, World!"})

@app.route("/add-admin/<string:username>")
def add_admin(username):
    res = ctrl.add_admin({"username": username, "password": "pass"})

    if res:
        return 201
    else:
        return 404

