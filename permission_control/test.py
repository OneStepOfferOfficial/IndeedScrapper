# coding:utf-8
"""
测试脚本
"""
import requests


session = requests.Session()


# login
login_url = 'http://localhost:9001/login'
# john is a user, mary is a merchant, admin is an admin
login_data = dict(name='admin', password='22222222')
login_request = session.post(login_url, json=login_data)
print(login_request.json())


# user_manage
user_manage_url = 'http://localhost:9001/user-manage'
login_request = session.post(user_manage_url)
if login_request:
    print(login_request.json())
else:
    print("Sorry, permission denied for page \"user_manage\".")


# merchant_manage
merchant_manage_url = 'http://localhost:9001/merchant-manage'
login_request = session.post(merchant_manage_url)
if login_request:
    print(login_request.json())
else:
    print("Sorry, permission denied for page \"merchant_manage\".")


# permission_manege
permission_manage_url = 'http://localhost:9001/permission-manage'
login_request = session.post(permission_manage_url)
if login_request:
    print(login_request.json())
else:
    print("Sorry, permission denied for page \"permission_manage\".")
