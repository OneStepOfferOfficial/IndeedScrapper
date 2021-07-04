from main import db
from todos import Todos

db.create_all()

rec_1 = Todos(task_name = "task 1", status = "In Progress")
rec_2 = Todos(task_name = "task 2", status = "Complete")
rec_3 = Todos(task_name = "task 3", status = "Todo")

db.session.add(rec_1)
db.session.add(rec_2)
db.session.add(rec_3)
db.session.commit()