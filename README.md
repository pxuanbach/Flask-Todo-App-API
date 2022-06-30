# Flask-Todo-App-API
## How to run?
1. Open Terminal in this directory.
2. Initialize the virtual environment by command: 
```{initialize the virtual environment}
python -m venv venv
```
3. Use this virtual environment by the activation command:
```
venv\Scripts\activate
```
4. Install package in `(venv) $`
```
pip install flask
pip install python-dotenv
```
5. Write the environment variable name and value in a file named .flaskenv located in the top-level directory of the project
```
FLASK_APP=run.py
```
6. Run project
```
flask run
```

## API
1. `/todo/new` - Create a new todo
- Method: POST
- Body:
```
{ "todo": "value" }
```
- Response: 
    - 200 OK
    ```
    {
        "todo": "value",
        "status": "Not Started"
    }
    ```
    - 400
    ```
    { "error": "Todo not added - value" }
    ```
2. `/todo/all` - Shows a list of all todos
- Method: GET
- Response:
    - 200 OK
    ```
    {
        "count": 2,
        "todos": [
            [
                2,              // id
                "Post todo",    // todo
                "Not Started"   // status
            ],
            [
                3,
                "hello world",
                "Not Started"
            ]
        ]
    }
    ```
3. `/todo/{todo_id}` - Show a single todo item
- Method: GET
- Path parameters: 
    - todo_id: int
- Response: 
    - 200 OK
    ```
    [
        2,
        "Post todo",
        "Not Started"
    ]
    ```
    - 400
    ```
    { "error": "Todo not found" }
    ```
4. `/todo/{todo_id}` - Update a todo given its identifier
- Method: PUT
- Path parameters: 
    - todo_id: int
- Body:
```
{ 
    "todo": "value",
    "status": "completed"   // Not Started, In Progress, Completed 
}
```
- Response:
    - 200 OK
    ```
    {
        "id": 4,
        "todo": "value",
        "status": "Completed"
    }
    ```
    - 400
    ```
    { "error": "Can't update todo" }
    ```
5. `/todo/{todo_id}` - Delete a todo given its identifier
- Method: DELETE
- Path parameters: 
    - todo_id: int
- Response:
    - 200 OK
    ```
    {
        "Message": "Delete todo success",
        "todo_id": "4"
    }
    ```
    - 400
    ```
    { "error": "Can't delete todo" }
    ```