# coding:utf-8
"""
desc：项目所需的功能函数
"""
from app.models import Users
from sqlalchemy.sql import text


def judgemember(name, email):
    error = []
    names = Users.query.add_columns(text('name'), text('id')).filter_by(name=name).first()
    emails = Users.query.add_columns(text('email'), text('id')).filter_by(email=email).first()
    if names:
        error.append("The user name %s is used"%name)
    if emails:
        error.append("The user email %s is used"%email)
    return error
