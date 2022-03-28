from flask import Flask, jsonify


app = Flask(__name__)



@app.route('/hello')
def hello_world():
    return jsonify({"data": "Hello, World!"})