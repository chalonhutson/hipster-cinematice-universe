from flask import Flask, jsonify
from model import Users_info


app = Flask(__name__)



@app.route('/')
def hello_world():
    return {"data": "Hello, World!"}