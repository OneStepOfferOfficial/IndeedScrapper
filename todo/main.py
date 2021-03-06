from flask import render_template, request, jsonify
import database as db_helper

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/appdb'

db = SQLAlchemy(app)



@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
	try:
		db_helper.remove_task_by_id(task_id)
		result = {'success': True, 'response': 'Removed task'}
	except:
		result = {'success': False, 'response': 'Something went wrong'}

	return jsonify(result)

@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
	data = request.get_json()
	print(data)
	try:
		if "status" in data:
			# db_helper.update_status_entry(task_id, data["status"])
			result = {'success': True, 'response': 'Status Updated'}
		elif "description" in data:
			# db_helper.update_task_entry(task_id, data["description"])
			result = {'success': True, 'response': 'Task Updated'}
		else:
			result = {'success': True, 'response': 'Nothing Updated'}
	except:
		result = {'success': False, 'response': 'Something went wrong'}

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
   app.run(port=5001, debug=True) # application will start listening for web request on port 5000