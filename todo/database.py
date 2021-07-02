import json

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


# task description update support
def update_task_entry(task_id, description):
	todo_list = []
	with open('todos.json', 'r') as json_file:
		todo_list = json.load(json_file)
		for task in todo_list:
		    if task["id"] == task_id:
			    task["task"] = description

	with open('todos.json', 'w') as outfile:
		json.dump(todo_list, outfile)


# task status update support
def update_status_entry(task_id, status):
    todo_list = []
    with open('todos.json', 'r') as json_file:
	    todo_list = json.load(json_file)
	    for task in todo_list:
		    if task["id"] == task_id:
			    task["status"] = status

    with open('todos.json', 'w') as outfile:
	    json.dump(todo_list, outfile)