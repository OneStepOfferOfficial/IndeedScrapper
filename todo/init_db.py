from flask import render_template, request, jsonify
import database as db_helper

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import Task
from main import db

task1 = Task(name='Task 1', status='Todo')
task2 = Task(name='Task 2', status='Todo')

db.session.add(task1)
db.session.add(task2)
db.session.commit()

print(Task.query.all())