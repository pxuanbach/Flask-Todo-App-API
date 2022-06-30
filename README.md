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