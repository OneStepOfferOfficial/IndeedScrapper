# coding:utf-8
"""
测试脚本
"""
import requests


session = requests.Session()

# login
login_url = 'http://localhost:9001/login'
login_data = dict(name='mary', password='22222222')
login_request = session.post(login_url, json=login_data)
print(login_request.json())

# user_manage
user_manage_url = 'http://localhost:9001/user-manage'
login_request = session.post(user_manage_url)
print(login_request.json())

# permission_manege
permission_manage_url = 'http://localhost:9001/permission-manage'
login_request = session.post(permission_manage_url)
print(login_request.json())
