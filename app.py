from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient
import os

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")
    db = client["animal_db"]
    return db

@app.route('/version')
def get_version():
    return "Version: 1.0"

@app.route('/world')
def get_world():
    db=""
    try:
        db = get_db()
        _world = db.world.find()
        cities = [ { "_id" : city["id"], "city" : city["city"], "loc" : city["loc"], "pop" : city["pop"], "state" : city["state"] } for city in _world]
        # return jsonify({"cities": db.world.find()})
        return jsonify({"cities":str(_world)})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

@app.route('/animals')
def get_stored_animals():
    db=""
    try:
        db = get_db()
        _animals = db.animal_tb.find()
        animals = [{"id": animal["id"], "name": animal["name"], "type": animal["type"]} for animal in _animals]
        return jsonify({"animals": animals})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

@app.route('/')
def hello_world():
    return jsonify({"about" : "this is python flask running in a docker container."})

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')