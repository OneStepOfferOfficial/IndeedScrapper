# this is a model for table "todos" in database "todolist"
from main import db

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task_name = db.Column(db.String(100), nullable = False)
    status = db.Column(db.String(20), nullable = False)

    def __repr__(self):
        return f"id: {self.id}, task_name: {self.task_name}, status: {self.status}."