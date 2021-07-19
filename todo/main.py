from flask import render_template, request, jsonify
from getpass import getpass
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# weird to have to run these lines twice even not under 'debug' mode
USERNAME = "postgres"
PASSWORD = getpass(f"please input the password for user {USERNAME}:") 


app = Flask(__name__)
app.config['DEBUG'] = False
# associate flask instance with a prebuilt database in postgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USERNAME}:{PASSWORD}@localhost/todolist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


# to avoid circular import when running init_table.py
import database as db_helper

@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    try:
        db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
        print(result)
    except:
        result = {'success': False, 'response': 'Something went wrong'}
        print(result)

    return jsonify(result)

@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    data = request.get_json()
    print(data)
    result = {}
    try:
        if "status" in data:
            db_helper.update_status_entry(task_id, data["status"]) # implemented in database.py
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
        print(result)
    except Exception as e:
        result = {'success': False, 'response': 'Something went wrong'}
        print(result, str(e))
    
    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    data = request.get_json()
    db_helper.insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = db_helper.fetch_todo()
    return render_template("index.html", items=items)



if __name__ == '__main__': 
   app.run(port=5001) # application will start listening for web request on port 5000