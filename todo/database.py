import json
from main import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.name

def fetch_todo():
	with open('todos.json', 'r') as json_file:
		todo_list = json.load(json_file)
		return todo_list

def insert_new_task(description):
	todo_list = []
	with open('todos.json', 'r') as json_file:
		todo_list = json.load(json_file)
	ids = [item["id"] for item in todo_list]
	new_id = max(ids) + 1
	todo_list.append({"id": new_id, "task": description, "status": "Todo"})
	
	with open('todos.json', 'w') as outfile:
		json.dump(todo_list, outfile)

def remove_task_by_id(task_id):
	todo_list = []
	with open('todos.json', 'r') as json_file:
		todo_list = json.load(json_file)
	for task in todo_list:
		if task["id"] == task_id:
			todo_list.remove(task)
	
	with open('todos.json', 'w') as outfile:
		json.dump(todo_list, outfile)

	