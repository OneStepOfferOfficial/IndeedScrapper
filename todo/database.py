from main import db
from model_todos import Todos


def fetch_todo():
    todo_list = []
    for instance in Todos.query.order_by(Todos.id).all():
        mapping = {"id": instance.id, "task": instance.task_name, "status": instance.status}
        todo_list.append(mapping)

    return todo_list


def insert_new_task(description):
    new_rec = Todos(task_name = description, status = "Todo")
    db.session.add(new_rec)
    db.session.commit()


def remove_task_by_id(task_id):
    rec = Todos.query.get(task_id)
    db.session.delete(rec)
    db.session.commit()


# task description update support
def update_task_entry(task_id, description):
    rec = Todos.query.get(task_id)
    rec.task_name = description
    db.session.commit()


# task status update support
def update_status_entry(task_id, status):
    rec = Todos.query.get(task_id)
    rec.status = status
    db.session.commit()