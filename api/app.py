from flask import Flask, jsonify, request
from flask_cors import CORS
import db
import json

app = Flask(__name__)
CORS(app)

with open('api/data/tasks.json', 'r') as data:
    tasks = json.loads(data.read())

@app.route('/api/task', methods=['GET'])
def getAll():
    return jsonify(tasks)

@app.route('/api/task/create', methods=['POST'])
def crateTask():
    reqData = request.get_json()
    tasks.append(reqData)
    return jsonify(reqData)

@app.route('/api/task/update', methods=['PUT'])
def updateTask():
    return 'Update task'

@app.route('/api/task/delete', methods=['DELETE'])
def deleteTask():
    return 'Delete task'

datat = db.get_databse('crud_py')
collection = datat['itens']

@app.route('/db', methods=['GET'])
def db():
    dump(collection.find())
    # print(jsonify(collection.find()))