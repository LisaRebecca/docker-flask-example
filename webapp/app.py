from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient
import os

app = Flask(__name__)

@app.route('/version')
def get_version():
    return "Version: 1.1"

@app.route('/')
def hello_world():
    return "I am the sample webapp."

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')