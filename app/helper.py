import sqlite3

DB_PATH = './app/todo.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

def create_table():
    try: 
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS "todos"
            (
                "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                "todo" TEXT NOT NULL, 
                "status" TEXT NOT NULL
            )''')
        conn.commit()
    except Exception as e:
        print('Error: ', e)
        return None

def add_todo(todo):
    try:
        create_table()
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('insert into todos(todo, status) values(?,?)', (todo, NOTSTARTED))
        conn.commit()
        return {"todo": todo, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None

def get_all_todos():
    try:
        create_table()
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from todos')
        rows = c.fetchall()
        return {"count": len(rows), "todos": rows}
    except Exception as e:
        print('Error: ', e)
        return None

def get_todo(id):
    try:
        create_table()
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from todos where id=?', str(id))
        todo = c.fetchone()
        return todo
    except Exception as e:
        print('Error: ', e)
        return None

def update_todo(id: str, todo: str, status: str): 
    if (status.lower().strip() == NOTSTARTED.lower()):
        status = NOTSTARTED
    elif (status.lower().strip() == INPROGRESS.lower()):
        status = INPROGRESS
    elif (status.lower().strip() == COMPLETED.lower()):
        status = COMPLETED
    else:
        print("Invalid status: " + status)
        return None

    try:
        create_table()
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('update todos set todo=?, status=? where id=?', (todo, status, id))
        conn.commit()
        return {"id": id, "todo": todo, "status": status}
    except Exception as e:
        print('Error: ', e)
        return None

def delete_todo(id: str): 
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from todos where id=?', (id))
        conn.commit()
        return {"Message": "Delete todo success", 'todo_id': id}
    except Exception as e:
        print('Error: ', e)
        return None