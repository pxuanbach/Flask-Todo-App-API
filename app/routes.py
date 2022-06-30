import json
from flask import Response, request
from app import app
from app import helper

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/todo/new', methods=['POST'])
def add_todo():
    req_data = request.get_json()
    # print(req_data)
    todo = req_data['todo']
    # print(todo)

    res_data = helper.add_todo(todo)
    if res_data is None:
        response = Response("{'error': 'Todo not added - '" + todo + "'}", status=400, mimetype='application/json')
        return response
    
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

@app.route('/todo/all')
def get_all_todos(): 
    res_data = helper.get_all_todos()

    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

@app.route('/todo/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    # print(todo_id)
    res_data = helper.get_todo(todo_id)
    if res_data is None:
        response = Response("{'error': 'Todo not found'}", status=400, mimetype='application/json')
        return response

    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

@app.route('/todo/update', methods=['PUT'])
def update_todo():
    req_data = request.get_json()
    todo_id = req_data['id']
    todo = req_data['todo']
    status = req_data['status']

    res_data = helper.update_todo(todo_id, todo, status)
    if res_data is None:
        response = Response("{'error': 'Can't update todo'}", status=400, mimetype='application/json')
        return response

    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

@app.route('/todo/delete', methods=['DELETE'])
def delete_todo():
    req_data = request.get_json()
    todo_id = req_data['id']

    res_data = helper.delete_todo(str(todo_id))
    if res_data is None:
        response = Response("{'error': 'Can't delete todo'}", status=400, mimetype='application/json')
        return response

    response = Response(json.dumps(res_data), mimetype='application/json')
    return response
